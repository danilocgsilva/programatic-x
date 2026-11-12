import pyautogui
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface
from programatic_x.Image import Image
from programatic_x.exceptions.CouldNotLocateStartButton import CouldNotLocateStartButton

class WindowsButtonStart(ButtonStartInterface):
    def click(self):
        try:
            image_center = Image.get_center("windows11_start_menu_150.png", 0.8)
            pyautogui.click(image_center)
        except pyautogui.ImageNotFoundException as e:
            try:
                image_center = Image.get_center("windows11_start_menu_100.png", 0.8)
                pyautogui.click(image_center)
            except pyautogui.ImageNotFoundException as e:
                raise CouldNotLocateStartButton("The start button could not be found.")
