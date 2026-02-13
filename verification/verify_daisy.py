import sys
import os
import subprocess
import time
from playwright.sync_api import sync_playwright

def verify_daisy():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Start server
        server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

        try:
            page.goto("http://localhost:8000/index.html")

            # Locate Daisy's image
            img = page.locator('img[src*="id=55"]')

            # Check attributes
            width = img.get_attribute("width")
            height = img.get_attribute("height")

            print(f"Daisy's image width: {width}")
            print(f"Daisy's image height: {height}")

            if width == "300" and height == "225":
                print("Attributes correct!")
            else:
                print("Attributes missing or incorrect!")

            # Take screenshot of the card
            # Locate the card containing Daisy
            card = page.locator('.card', has=img)
            # Wait for image to load to get a nice screenshot
            try:
                page.wait_for_function('document.querySelector(\'img[src*="id=55"]\').complete')
            except:
                pass
            card.screenshot(path="/home/jules/verification/daisy_card.png")
            print("Screenshot saved to /home/jules/verification/daisy_card.png")

        finally:
            server_process.terminate()
            server_process.wait()
            browser.close()

if __name__ == "__main__":
    # Kill any existing server
    subprocess.run(["pkill", "-f", "http.server"], check=False)
    verify_daisy()
