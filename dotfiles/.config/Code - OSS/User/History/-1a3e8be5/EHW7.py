from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        # Launch browser (non-headless to see what's happening)
        browser = p.chromium.launch(headless=False, args=['--no-sandbox'])

        # Create a new page
        page = browser.new_page()

        # Go to the target URL with a timeout of 1 minute
        page.goto("https://play.ttrockstars.com/gamel/play/garage", timeout=10000000)
