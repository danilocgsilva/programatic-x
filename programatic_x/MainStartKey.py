import time
import subprocess
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface

class MainStartKey(ButtonStartInterface):
    def click(self):
        time.sleep(3)
        subprocess.run(['ydotool', 'key', '125:1', '31:1', '31:0', '125:0'])