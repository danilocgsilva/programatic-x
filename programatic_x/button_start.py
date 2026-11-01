from abc import ABC, abstractmethod
import pyautogui
from ButtonStartInterface import ButtonStartInterface

class WindowsButtonStart(ButtonStartInterface):
    def click(self):
        screen_width, screen_height = pyautogui.size()
        pyautogui.click(10, screen_height - 10)
