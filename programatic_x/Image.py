from importlib.resources import files
import pyautogui

class Image:
    @staticmethod
    def get_image_path(
        image_name: str, 
        package_path: str = "programatic_x",
        relative_path: str = "assets"
    ) -> str:
        """
        Returns the absolute path to an image in the assets folder.
        Uses importlib.resources to ensure the path is correct 
        even when the package is installed in site-packages.
        """
        # Get the path to the 'programatic_x' package directory
        package_dir = files(package_path)
        # Join the 'assets' folder and the image name
        image_path = package_dir.joinpath(relative_path, image_name)
        return str(image_path)

    @staticmethod
    def get_center(
        image_name: str, 
        confidence=0.6,
        package_path: str = "programatic_x",
        relative_path: str = "assets"
    ):
        image_path = Image.get_image_path(image_name, package_path, relative_path)
        
        # pyautogui.locateOnScreen will raise ImageNotFoundException if confidence is used and it fails
        image_location = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=True)
        
        if image_location is not None:
            return pyautogui.center(image_location)
        else:
            # Raise the specific exception that WindowsButtonStart expects
            raise pyautogui.ImageNotFoundException(f"{image_name} not found on the screen.")