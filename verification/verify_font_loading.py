import subprocess
import time
import sys
from playwright.sync_api import sync_playwright

def verify_fonts_and_screenshot():
    # Start server
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8081"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2) # Wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Navigate
            page.goto("http://localhost:8081")

            # Wait for fonts
            page.evaluate("document.fonts.ready")

            # Check fonts are loaded
            fonts_to_check = ["16px Lato", "700 16px Montserrat", "16px Lexend"]
            all_loaded = True
            for font in fonts_to_check:
                loaded = page.evaluate(f"document.fonts.check('{font}')")
                print(f"Font {font} loaded: {loaded}")
                if not loaded:
                    all_loaded = False

            if not all_loaded:
                print("FAIL: Fonts not loaded correctly.")
            else:
                print("SUCCESS: Fonts loaded correctly.")

            # Take screenshot
            screenshot_path = "verification/font_verification.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

            browser.close()

    finally:
        server_process.terminate()

if __name__ == "__main__":
    verify_fonts_and_screenshot()
