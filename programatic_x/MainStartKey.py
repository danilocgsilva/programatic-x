import pyautogui
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface

class MainStartKey(ButtonStartInterface):
    def click(self):
        pyautogui.hotkey('super', 's')
