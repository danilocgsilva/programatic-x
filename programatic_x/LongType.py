from programatic_x.interfaces.LontTypeInterface import LontTypeInterface
from pynput.keyboard import Controller
# from time import sleep

class LongType(LontTypeInterface):
    def type(self, text_to_type: str):
        keyboard = Controller()
        for s in text_to_type:
            keyboard.type(s)
            # sleep(0.0015)
