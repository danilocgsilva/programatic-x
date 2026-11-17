from programatic_x.interfaces.LontTypeInterface import LontTypeInterface
from pynput.keyboard import Controller
from time import sleep

class LongType(LontTypeInterface):
    def type(self, text_to_type: str, milliseconds: int = 1):
        sleep_time_milliseconds = milliseconds / 1000
        keyboard = Controller()
        for s in text_to_type:
            keyboard.type(s)
            sleep(sleep_time_milliseconds)
