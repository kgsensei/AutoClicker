import pyautogui as pya
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        pya.click(button='right')

with mouse.Listener(on_click=on_click) as listener:
    listener.join()