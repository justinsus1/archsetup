from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pyautogui
from pynput import keyboard
import time

combination = {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode.from_char('t')}
current_keys = set()

key_combination_pressed = False

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
        print("No text found")
        return None
    
    else:
        print("Text: ", text)
    return text

def type(text):
    pyautogui.typewrite(text, interval=0.01)

def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://play.typeracer.com/")

    text_type = get_text(driver)
    if text_type:
        type(text_type)

main()
