import pyautogui
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface

class WindowsButtonStart(ButtonStartInterface):
    def click(self):
        screen_width, screen_height = pyautogui.size()
        pyautogui.click(10, screen_height - 10)
