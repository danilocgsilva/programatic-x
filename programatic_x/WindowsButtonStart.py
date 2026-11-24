import pyautogui
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface
from programatic_x.Image import Image
from programatic_x.exceptions.CouldNotLocateStartButton import CouldNotLocateStartButton
from time import sleep

class WindowsButtonStart(ButtonStartInterface):
    def click(self, smooth_time: int = 0, click_await: int = 0):
        """Click the Windows start button using image recognition."""
        image_configs = [
            ("windows11_start_menu_100_dark.png", 0.8),
            ("windows11_start_menu_150_dark.png", 0.8),
            ("windows11_start_menu_100_light.png", 0.8),
            ("windows11_start_menu_150_light.png", 0.8)
        ]
        image_instance = Image()
        for image_path, confidence in image_configs:
            try:
                image_centers = image_instance.get_centers(image_path, confidence)
                image_center = image_centers[0]
                if smooth_time == 0:
                    if not click_await == 0:
                        sleep(click_await)
                    pyautogui.click(image_center)
                else:
                    pyautogui.moveTo(image_center[0], image_center[1], smooth_time)
                    if not click_await == 0:
                        sleep(click_await)
                    pyautogui.click()
                return
            except pyautogui.ImageNotFoundException:
                continue
        
        raise CouldNotLocateStartButton("The start button could not be found.")
