from programatic_x.interfaces.LontTypeInterface import LontTypeInterface
import pyautogui

class LongType(LontTypeInterface):
    def type(self, text_to_type: str):
        pyautogui.write(text_to_type)
