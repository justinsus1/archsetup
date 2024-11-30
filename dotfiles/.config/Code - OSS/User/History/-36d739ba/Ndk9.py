from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"  # Address of the running browser

# Connect to the existing browser
driver = webdriver.Chrome(options=options)

# List all open tabs
print("Current tabs:")
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(f"Tab URL: {driver.current_url}")

# Interact with a specific tab
driver.switch_to.window(driver.window_handles[0])  # Switch to the first tab
print(f"Interacting with tab: {driver.current_url}")
driver.find_element("id", "button").click()  # Example interaction
