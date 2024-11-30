from playwright.sync_api import sync_playwright

oper = ""
n = []

with sync_playwright() as p:
    try:
        # Launch the browser with --no-sandbox flag to bypass possible OS compatibility issues
        browser = p.chromium.launch(headless=False, args=['--no-sandbox'])

        # Create a new page
        page = browser.new_page()

        # Go to the target URL with a timeout of 60 seconds
        page.goto("https://play.ttrockstars.com/gamel/play/garage", timeout=60000)  # 1 minute timeout
        page.wait_for_load_state('load')  # Wait for the page to finish loading

        # Wait for the elements (span) to be available with a timeout of 30 seconds
        page.wait_for_selector("span", timeout=30000)

        # Query all "span" elements
        characters = page.query_selector_all("span")

        # Extract text content and manipulate it
        for char in characters:
            text = char.inner_text()  # Get the text inside the element
            if text == "×":
                oper = "multi"
            elif text.isdigit():  # Check if the text is an integer
                n.append(int(text))
            elif text == "÷":
                oper = "div"

        # Perform the calculation based on the operation
        if oper == "multi" and len(n) >= 2:
            ans = n[0] * n[1]
        elif oper == "div" and len(n) >= 2:
            ans = n[0] / n[1]
        else:
            ans = 0  # Default in case of no valid operation

        # Find the input box and fill it with the calculated answer
        search_box = page.query_selector('input[name="input-holder width-100"]')
        search_box.fill(str(ans))  # Fill the input field with the answer
        search_box.press("Enter")  # Submit the answer

    except Exception as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Close the browser after the operation
        browser.close()
