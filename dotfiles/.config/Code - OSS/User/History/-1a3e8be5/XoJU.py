from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch Chromium
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    # Perform your actions here (optional)

    # Remove or comment out this line to keep the browser open
    # browser.close()
