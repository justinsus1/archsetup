import logging
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Firefox()
driver.get("http://www.python.org")
print(driver.title)
driver.quit()
