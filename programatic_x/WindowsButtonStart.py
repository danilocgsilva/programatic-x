import pyautogui
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface
from programatic_x.Image import Image
from programatic_x.exceptions.CouldNotLocateStartButton import CouldNotLocateStartButton

class WindowsButtonStart(ButtonStartInterface):
    def click(self):
        """Click the Windows start button using image recognition."""
        # Define fallback image paths with their confidence thresholds
        image_configs = [
            ("windows11_start_menu_100_dark.png", 0.8),
            ("windows11_start_menu_100_light.png", 0.8),
            ("windows11_start_menu_150_light.png", 0.8)
        ]
        
        for image_path, confidence in image_configs:
            try:
                image_center = Image.get_center(image_path, confidence)
                pyautogui.click(image_center)
                return  # Success - exit early
            except pyautogui.ImageNotFoundException:
                continue  # Try the next image configuration
        
        # If we reach here, all attempts failed
        raise CouldNotLocateStartButton("The start button could not be found.")
