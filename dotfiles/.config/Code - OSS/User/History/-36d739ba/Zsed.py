from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    n = []
    # Navigate to a website
    page.goto("https://play.ttrockstars.com/gamel/play/garage")
    
    # Interact with elements
    characters = page.query_selector_all("span")
    while len(n) < 1 and len(oper) < 1:
        if characters == "×":
            oper = "multi"
        if characters.is_interger():
            n.append(characters)
        if characters == "÷":
            oper = "div"
    
    if oper == "multi":
        ans = n[0] * n[1]
    else:
        ans = n[0] / n[1]

    search_box = page.query_selector("input[name='']")
    search_box.fill("playwright")
    search_box.press("Enter")

    # Extract results
    results = page.query_selector_all(".result")
    for result in results:
        print(result.inner_text())

    browser.close()

from playwright.sync_api import sync_playwright

def read_content():
    # Start a Playwright session
    with sync_playwright() as p:
        # Launch the browser (headless is True to run in the background without UI)
        browser = p.chromium.launch(headless=True)
        
        # Open a new page in the browser
        page = browser.new_page()
        
        # Go to the URL you want to scrape
        page.goto('https://example.com')

        # Wait for the page to load (you can use specific selectors to ensure elements are loaded)
        page.wait_for_selector('h1')  # Wait until an <h1> element is visible

        # Read the content (e.g., reading text from an <h1> tag)
        title = page.inner_text('h1')  # Get text from <h1>
        print(f"Page Title: {title}")

        # Extract other text or elements (e.g., paragraphs, links)
        paragraphs = page.query_selector_all('p')  # Get all <p> elements
        for p in paragraphs:
            print(p.inner_text())  # Print text inside each <p> tag

        # Close the browser after the task is complete
        browser.close()

# Call the function to read content
read_content()

# ×
