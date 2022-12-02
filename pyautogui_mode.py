import pyautogui, pyperclip, keyboard
from time import sleep

screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
# print(currentMouseX, currentMouseY)


with pyautogui.hold('win'):
    pyautogui.press('r')

pyautogui.moveTo(203, 277)
pyautogui.click()
sleep(1)
pyautogui.moveTo(960, 540, duration=1)
pyautogui.click()
sleep(1)
keyboard.write('''''', delay=0.01)