from selenium import webdriver

# Assuming GeckoDriver is installed and available in the system PATH
driver = webdriver.Firefox()
driver.get("http://www.python.org")
print(driver.title)
driver.quit()
