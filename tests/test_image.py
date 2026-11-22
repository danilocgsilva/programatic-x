import pytest
from unittest.mock import patch
import numpy as np
import pyautogui
from programatic_x.Image import Image

def test_get_center_success(mock_pyautogui):
    image_instance = Image()
    image_instance.template = np.zeros((20, 40), dtype=np.uint8)
    image_instance.max_val = 0.9
    image_instance.max_loc = (80, 120)

    with patch.object(image_instance, "compare"):
        result = image_instance.get_center("test.png")

    assert result == (100, 130)

def test_get_center_not_found(mock_pyautogui):
    image_instance = Image()
    image_instance.template = np.zeros((20, 40), dtype=np.uint8)
    image_instance.max_val = 0.5
    image_instance.max_loc = (80, 120)

    with patch.object(image_instance, "compare"):
        with pytest.raises(pyautogui.ImageNotFoundException):
            image_instance.get_center("test.png", confidence=0.75)