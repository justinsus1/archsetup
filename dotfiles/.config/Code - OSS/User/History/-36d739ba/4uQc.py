from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Use Chromedriver
driver = webdriver.Chrome()  # Or use webdriver.Firefox() if using Firefox

# Open Google
driver.get("https://www.google.com")

# Interact with the search box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium automation on Arch Linux" + Keys.RETURN)

# Print page title
print(driver.title)

# Quit the browser
driver.quit()
