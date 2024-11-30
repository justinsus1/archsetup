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

# def on_press(key):
#     global key_combination_pressed
#     if key in combination:
#         current_keys.add(key)
#         if all(k in current_keys for k in combination):  # If all keys in combination are pressed
#             print("Ctrl + Alt + T detected!")
#             key_combination_pressed = True  # Set the flag to True to indicate the combo was pressed
#             return False  # Stop the listener

# def on_release(key):
#     if key in combination:
#         current_keys.remove(key)

def main():
    global key_combination_pressed
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://play.typeracer.com/")

    # # Start listening for the key combination in the background
    # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    #     while not key_combination_pressed:  # Wait until the key combination is pressed
    #         time.sleep(0.1)  # Avoid high CPU usage while waiting
    #     listener.stop()  # Stop the listener once the combination is pressed
    
    # Now the rest of the script can run

    time.sleep(5)

    text_type = get_text(driver)
    if text_type:
        type(text_type)

main()
