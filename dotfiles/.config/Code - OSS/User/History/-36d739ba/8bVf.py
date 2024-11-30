from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to a website
    page.goto("https://example.com")
    
    # Interact with elements
    search_box = page.query_selector("input[name='q']")
    search_box.fill("playwright")
    search_box.press("Enter")

    # Extract results
    results = page.query_selector_all(".result")
    for result in results:
        print(result.inner_text())

    browser.close()
