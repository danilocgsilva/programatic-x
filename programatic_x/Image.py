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
    
    @template.setter(self, template)
    def template(self, template):
        self._template = template
    
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

    # @staticmethod
    # def get_center(
    #     image_name: str, 
    #     confidence=0.6,
    #     package_path: str = "programatic_x",
    #     relative_path: str = "assets"
    # ):
    #     image_path = Image.get_image_path(image_name, package_path, relative_path)
        
    #     # pyautogui.locateOnScreen will raise ImageNotFoundException if confidence is used and it fails
    #     image_location = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=True)
        
    #     if image_location is not None:
    #         return pyautogui.center(image_location)
    #     else:
    #         # Raise the specific exception that WindowsButtonStart expects
    #         raise pyautogui.ImageNotFoundException(f"{image_name} not found on the screen.")
        
        
    def get_center(
        self,
        image_name: str,
        confidence=0.75,
        package_path="programatic_x",
        relative_path="assets"
    ):
        # image_path = Image.get_image_path(
        #     image_name,
        #     package_path,
        #     relative_path
        # )

        # template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # if template is None:
        #     raise FileNotFoundError(image_path)

        # screenshot = np.array(pyautogui.screenshot())
        # screenshot = cv2.cvtColor(
        #     screenshot,
        #     cv2.COLOR_RGB2GRAY
        # )

        # result = cv2.matchTemplate(
        #     screenshot,
        #     template,
        #     cv2.TM_CCOEFF_NORMED
        # )

        # _, max_val, _, max_loc = cv2.minMaxLoc(result)
        
        self.compare(image_name, package_path, relative_path)

        if self.max_val < confidence:
            raise pyautogui.ImageNotFoundException(
                f"{image_name} not found. Score: {self.max_val:.4f}"
            )

        height, width = self.template.shape

        center_x = self.max_loc[0] + width // 2
        center_y = self.max_loc[1] + height // 2

        return center_x, center_y
    
    def compare(
        self,
        image_name: str,
        package_path="programatic_x",
        relative_path="assets"
    ):
        image_path = Image.get_image_path(
            image_name,
            package_path,
            relative_path
        )

        self.template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if self.template is None:
            raise FileNotFoundError(image_path)

        screenshot = np.array(pyautogui.screenshot())
        screenshot = cv2.cvtColor(
            screenshot,
            cv2.COLOR_RGB2GRAY
        )

        result = cv2.matchTemplate(
            screenshot,
            self.template,
            cv2.TM_CCOEFF_NORMED
        )

        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        self.max_val = max_val
        self.max_loc = max_loc
