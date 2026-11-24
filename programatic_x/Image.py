from importlib.resources import files
import pyautogui
import cv2
import numpy as np

class Image:   
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
        confidence: float = 0.9,
        package_path: str = "programatic_x",
        relative_path: str = "assets"
    ):
        screenshot = pyautogui.screenshot()

        screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        icon_path = self.get_image_path(
            image_name,
            package_path,
            relative_path,
        )
        
        icon = cv2.imread(icon_path, cv2.IMREAD_COLOR)

        if icon is None:
            raise FileNotFoundError(f"Could not load icon image: {icon_path}")

        icon_height, icon_width = icon.shape[:2]

        scores = cv2.matchTemplate(screen, icon, cv2.TM_CCOEFF_NORMED)

        ys, xs = np.where(scores >= confidence)

        centers_x = xs + (icon_width // 2)
        centers_y = ys + (icon_height // 2)
        return list(zip(centers_x.tolist(), centers_y.tolist()))
