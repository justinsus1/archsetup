from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Ensure the path to Chromedriver is correct
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()
