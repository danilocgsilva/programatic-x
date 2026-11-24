import pyautogui
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface
from programatic_x.Image import Image
from programatic_x.exceptions.CouldNotLocateStartButton import CouldNotLocateStartButton
from time import sleep

class WindowsButtonStart(ButtonStartInterface):
    def __init__(self, algorithm_confidence: float = 0.8):
        self._algorithim_confidence = algorithm_confidence
    
    def click(self, smooth_time: int = 0, click_await: int = 0):
        """Click the Windows start button using image recognition."""
        image_configs = [
            "windows11_start_menu_100_dark.png",
            "windows11_start_menu_150_dark.png",
            "windows11_start_menu_100_light.png",
            "windows11_start_menu_150_light.png"
        ]
        image_instance = Image()
        for image_path in image_configs:
            try:
                image_centers = image_instance.get_centers(image_path, self._algorithim_confidence)
                
                if len(image_centers) == 0:
                    raise pyautogui.ImageNotFoundException(f"Image not found: {image_path}")
                
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
