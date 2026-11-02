import platform
from programatic_x.WindowsButtonStart import WindowsButtonStart
from programatic_x.MainStartKey import MainStartKey

class ButtonStartFactory:
    @staticmethod
    def create_button_start() -> object:
        """
        Creates and returns the appropriate button start implementation 
        based on the operating system.
        
        Returns:
            ButtonStartInterface: Implementation for the current OS
        """
        os_name = platform.system().lower()
        
        if os_name == "windows":
            return WindowsButtonStart()
        else:
            # For all other operating systems, use the keyboard shortcut approach
            return MainStartKey()