import pyautogui
import time
import pyperclip
import platform
import subprocess


def open_wechat_moments():
    # Open WeChat (change the path to your WeChat installation if necessary)
    if platform.system() == 'Darwin':
        subprocess.run(["open", "-a", "WeChat"])  # For macOS
    elif platform.system() == 'Windows':
        subprocess.run(["start", "C:\\path\\to\\WeChat.exe"])  # Example for Windows
    # os.startfile("C:\\path\\to\\WeChat.exe")  # For Windows
    # Wait for WeChat to open
    # time.sleep(5)
    # print("current position1 ",pyautogui.position())
    # time.sleep(5)
    # print("current position2 ",pyautogui.position())
    # Move the mouse to the position of the Moments button and click
    # You should replace (x, y) with the actual coordinates
    time.sleep(1)
    pyautogui.click(x=527, y=382)  # Example coordinates for Moments button
    time.sleep(1)
    pyautogui.click(x=964, y=149) 
    time.sleep(2)


def prepare_input_field():
    # Clear the clipboard and simulate a paste action to ensure focus is on the input field
    pyperclip.copy("")
    if platform.system() == 'Darwin':
        pyautogui.hotkey('command', 'v', pressTime=0.1)
    elif platform.system() == 'Windows':
        pyautogui.hotkey('ctrl', 'v', pressTime=0.1)

def typewrite(char):
    # Function to type a single character
    pyperclip.copy(char)  # Copy the character to the clipboard
    if platform.system() == 'Darwin':
        pyautogui.hotkey('command', 'v', pressTime=0.1)  # Paste the character
    elif platform.system() == 'Windows':
        pyautogui.hotkey('ctrl', 'v', pressTime=0.1)  # Paste the character

def type_text(text):
    # Function to type the entire text character by character
    for char in text:
        print(char,end="")
        typewrite(char)
        time.sleep(0.1)

def main():
    prepare_input_field()
    # Define the text to be typed
    text_to_type = """你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
你要发朋友圈的文本
"""

    # Wait for the user to switch to the WeChat input field
    print("请将输入的焦点切换到微信朋友圈，然后不要移动鼠标")
    open_wechat_moments()
    # time.sleep(5)
    type_text(text_to_type)

if __name__ == "__main__":
    main()
