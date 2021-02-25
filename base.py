try:
    import pyautogui, keyboard
except Exception:
    import os
    os.system("pip install pyautogui")
    os.system("pip install keyboard")
    import pyautogui, keyboard

x=input("AutoClicker Key Bind: ")
while True:
    if keyboard.is_pressed(x):
        pyautogui.click(button='right')
