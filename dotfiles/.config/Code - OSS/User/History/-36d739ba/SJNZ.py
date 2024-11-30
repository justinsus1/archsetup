from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import keyboard
import time

def get_text(driver):
    time.sleep(1)
    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")
    span = soup.findAll("span")
    text = ""

    for i in span:
        if "unselectable" in str(i):
            text += i.text
    
    if not text:
        print("fuck")
        return None
    
    else:
        print("Text: ", text)
    return text

def type(text):
    pyautogui.typewrite(text, interval = 0.01)

def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options = chrome_options)
    driver.get("https://play.typeracer.com/")

    keyboard.wait("ctrl+alt+t")

    text_type = get_text(driver)
    if text_type:
        type(text_type)

main()