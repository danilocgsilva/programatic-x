import pyautogui
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface
from programatic_x.Image import Image

class WindowsButtonStart(ButtonStartInterface):
    def click(self):
        image_center = Image.get_center("windows11_start_menu_150.png", 0.6)
        pyautogui.click(image_center)
