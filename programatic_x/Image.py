from importlib.resources import files
import pyautogui
import cv2
import numpy as np
from typing import List
from programatic_x.named_tuples.Coordinate import Coordinate

class Image:
    centers: List[Coordinate]
    dimensions: List[Coordinate]  # Stores (width, height) for each detected icon

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
        package_dir = files(package_path)
        image_path = package_dir.joinpath(relative_path, image_name)
        return str(image_path)

    def compute(
        self, 
        image_name: str, 
        confidence: float = 0.9,
        package_path: str = "programatic_x",
        relative_path: str = "assets"
    ) -> Image:
        screenshot = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        icon_path = self.get_image_path(image_name, package_path, relative_path)
        icon = cv2.imread(icon_path, cv2.IMREAD_COLOR)

        if icon is None:
            raise FileNotFoundError(f"Could not load icon image: {icon_path}")

        icon_height, icon_width = icon.shape[:2]
        scores = cv2.matchTemplate(screen, icon, cv2.TM_CCOEFF_NORMED)
        ys, xs = np.where(scores >= confidence)

        centers_x = xs + (icon_width // 2)
        centers_y = ys + (icon_height // 2)
        self.centers = list(zip(centers_x.tolist(), centers_y.tolist()))

        # Create matching dimensions list for each detected center
        self.dimensions = [
            Coordinate(icon_width, icon_height)
            for _ in range(len(self.centers))
        ]

        return self

    def get_centers(
        self, 
        image_name: str, 
        confidence: float = 0.9,
        package_path: str = "programatic_x",
        relative_path: str = "assets"
    ) -> List[Coordinate]:
        self.compute(image_name, confidence, package_path, relative_path)
        return self.centers

    def get_dimensions(self) -> List[Coordinate]:
        """
        Returns the width and height of each detected icon.
        Each dimension corresponds to a detected center in the same order.
        """
        return self.dimensions
