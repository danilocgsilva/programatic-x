from importlib.resources import files
import pyautogui
import cv2
import numpy as np

class Image:
    @property
    def max_val(self):
        return self._max_val
    
    @max_val.setter
    def max_val(self, max_val: int):
        self._max_val = max_val
        
    @property
    def max_loc(self):
        return self._max_loc
    
    @max_loc.setter
    def max_loc(self, max_loc):
        self._max_loc = max_loc
        
    @property
    def template(self):
        return self._template
    
    @template.setter
    def template(self, template):
        self._template = template
    
    @property
    def screenshot(self):
        return self._screenshot
    
    @screenshot.setter
    def screenshot(self, screenshot):
        self._screenshot = screenshot
    
    def get_image_path(
        self,
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
        
    def get_centers(
        self,
        image_name: str,
        confidence: float = 0.75,
        package_path="programatic_x",
        relative_path="assets",
    ) -> list[tuple[int, int]]:
        image_path = self.get_image_path(
            image_name,
            package_path,
            relative_path,
        )
        screenshot = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        icon = cv2.imread(image_path, cv2.IMREAD_COLOR)

        if icon is None:
            raise FileNotFoundError(image_path)

        icon_height, icon_width = icon.shape[:2]
        scores = cv2.matchTemplate(screen, icon, cv2.TM_CCOEFF_NORMED)
        ys, xs = np.where(scores >= confidence)

        if len(xs) == 0:
            raise pyautogui.ImageNotFoundException(
                f"{image_name} not found at confidence {confidence:.4f}"
            )

        centers_x = xs + (icon_width // 2)
        centers_y = ys + (icon_height // 2)
        return list(zip(centers_x.tolist(), centers_y.tolist()))
