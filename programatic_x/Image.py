from importlib.resources import files as pkg_files

class Image:
    def __init__(self, name: str, pkg_name: Optional[str] = None):
        self.name = name
        self.pkg_name = pkg_name or __package__

        self._image_path = self._resolve_image_path()