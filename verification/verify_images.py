from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Open the local index.html
        url = "file://" + os.path.abspath("index.html")
        page.goto(url)

        # Wait for the images to be attached to the DOM
        page.wait_for_selector(".card-image img")

        # Verify image attributes for the first three images (the optimized ones)
        images = page.locator(".card-image img").all()

        # Monti (eager, 640x426)
        monti = images[0]
        assert "continental-bulldog-ge5a6148c6_640.jpg" in monti.get_attribute("src")
        assert monti.get_attribute("width") == "640"
        assert monti.get_attribute("height") == "426"
        assert monti.get_attribute("loading") is None # Default eager
        print("Monti verified")

        # Thor (lazy, 640x407)
        thor = images[1]
        assert "dog-g392687a52_640.jpg" in thor.get_attribute("src")
        assert thor.get_attribute("width") == "640"
        assert thor.get_attribute("height") == "407"
        assert thor.get_attribute("loading") == "lazy"
        print("Thor verified")

        # Bolt (lazy, 640x426)
        bolt = images[2]
        assert "weimaraner-g65bcb290c_640.jpg" in bolt.get_attribute("src")
        assert bolt.get_attribute("width") == "640"
        assert bolt.get_attribute("height") == "426"
        assert bolt.get_attribute("loading") == "lazy"
        print("Bolt verified")

        # Take a screenshot
        page.screenshot(path="verification/optimized_images.png")
        print("Screenshot saved to verification/optimized_images.png")

        browser.close()

if __name__ == "__main__":
    run()
