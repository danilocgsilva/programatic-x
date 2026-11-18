from programatic_x.interfaces.LontTypeInterface import LontTypeInterface
from pynput.keyboard import Controller, Key
from time import sleep

class LongType(LontTypeInterface):
    def type(
        self, 
        text_to_type: str, 
        milliseconds: int = 1, 
        shift_enter: bool = False
    ):
        sleep_time_milliseconds = milliseconds / 1000
        keyboard = Controller()
        text_to_type = text_to_type.replace('\r\n', '\n').replace('\r', '\n')

        for s in text_to_type:
            if shift_enter and s == '\n':
                with keyboard.pressed(Key.shift):
                    keyboard.tap(Key.enter)
            else:
                keyboard.type(s)
            sleep(sleep_time_milliseconds)
