from playwright.sync_api import sync_playwright

oper = ""
n = []

with sync_playwright() as p:
    try:
        # Launch browser (non-headless to see what's happening)
        browser = p.chromium.launch(headless=False, args=['--no-sandbox'])

        # Create a new page
        page = browser.new_page()

        # Go to the target URL with a timeout of 1 minute
        page.goto("https://play.ttrockstars.com/gamel/play/garage", timeout=60000)
        
        # Wait for the page to fully load by waiting for the main page element (e.g. body or any key selector)
        page.wait_for_selector("body", timeout=60000)  # Ensure the body of the page loads

        # Wait for specific elements (for example, elements that indicate page readiness)
        page.wait_for_selector('span', timeout=30000)  # Wait for any span element to load

        # Check for the elements to ensure they're available
        characters = page.query_selector_all("span")
        if not characters:
            print("No span elements found.")
            return

        # Extract text content and manipulate it
        for char in characters:
            text = char.inner_text()  # Get the text inside the element
            print(f"Text found: {text}")  # Debugging output to track found text

            if text == "×":
                oper = "multi"
            elif text.isdigit():  # Check if the text is an integer
                n.append(int(text))
            elif text == "÷":
                oper = "div
