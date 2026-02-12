import threading
import http.server
import socketserver
import os
import time
import pytest
from playwright.sync_api import sync_playwright

PORT = 8000
SERVER_URL = f"http://localhost:{PORT}"

class ThreadedHTTPServer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.server = None
        self.daemon = True

    def run(self):
        handler = http.server.SimpleHTTPRequestHandler
        socketserver.TCPServer.allow_reuse_address = True
        self.server = socketserver.TCPServer(("", PORT), handler)
        print(f"Serving at port {PORT}")
        self.server.serve_forever()

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()

@pytest.fixture(scope="module")
def server():
    server_thread = ThreadedHTTPServer()
    server_thread.start()
    time.sleep(1) # Give it a second to start
    yield server_thread
    server_thread.stop()

def test_csp_headers_and_resources(server):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Listen for console messages
        console_messages = []
        page.on("console", lambda msg: console_messages.append(msg))

        # Listen for page errors
        page_errors = []
        page.on("pageerror", lambda err: page_errors.append(err))

        page.goto(SERVER_URL)

        # Check title to ensure we loaded the right page
        assert "Adopt Time" in page.title()

        # Check for CSP meta tag
        csp_meta = page.locator('meta[http-equiv="Content-Security-Policy"]')
        assert csp_meta.count() > 0, "Content-Security-Policy meta tag is missing"

        # Verify no console errors related to CSP
        # CSP violations usually show up as console errors
        csp_errors = [msg.text for msg in console_messages if "Content Security Policy" in msg.text]
        assert len(csp_errors) == 0, f"CSP Errors found: {csp_errors}"

        # Verify images load
        # We can check if naturalWidth > 0 for all images
        images = page.locator("img")
        count = images.count()
        for i in range(count):
            img = images.nth(i)
            # Check if image loaded
            is_loaded = img.evaluate("img => img.complete && img.naturalWidth > 0")
            src = img.get_attribute("src")
            assert is_loaded, f"Image failed to load: {src}"

        browser.close()
