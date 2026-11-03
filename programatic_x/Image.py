from importlib.resources import files as pkg_files
import os
import pyautogui

class Image:
    @staticmethod
    def get_image_path(image_name: str):
        return os.path.join("assets", image_name)

    @staticmethod
    def get_center(image_name: str, confidence=0.6):
        image_path = Image.get_image_path(image_name)
        image_location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if image_location is not None:
            return pyautogui.center(image_location)
        else:
            raise Exception(f"{image_name} not found on the screen.")