from playwright.sync_api import sync_playwright

oper = ""
usrsat = False
with sync_playwright() as p:
    # Navigate to a website
    
    page.goto("https://play.ttrockstars.com/gamel/play/garage")
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    n = []  
    # Interact with elements
    characters = page.query_selector_all("span")
    
    while len(n) < 1 and oper != "":
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

        search_box = page.query_selector('input[name="input-holder width-100"]', ans)
        search_box.press("Enter")
