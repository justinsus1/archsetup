from playwright.sync_api import sync_playwright

oper = ""
n = []  
with sync_playwright() as p:
    # Launch the browser and create a page
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Go to the target URL
    page.goto("https://play.ttrockstars.com/gamel/play/garage")
    
    # Wait for elements to load before interacting
    page.wait_for_selector("span")
    
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

    # Close the browser after the operation
    browser.close()
