import pytest
from unittest.mock import patch
import numpy as np
import pyautogui
from programatic_x.Image import Image

def test_get_center_success(mock_pyautogui):
    image_instance = Image()
    mock_pyautogui.screenshot.return_value = np.zeros((100, 100, 3))

    with (
        patch.object(image_instance, "get_image_path", return_value="test.png"),
        patch("programatic_x.Image.cv2.cvtColor", side_effect=lambda image, _: image),
        patch(
            "programatic_x.Image.cv2.imread",
            return_value=np.zeros((20, 40, 3)),
        ),
        patch(
            "programatic_x.Image.cv2.matchTemplate",
            return_value=np.array([[0.9, 0.1], [0.1, 0.95]]),
        ),
    ):
        result = image_instance.get_center("test.png")

    assert result == [(20, 10), (21, 11)]

def test_get_center_not_found(mock_pyautogui):
    image_instance = Image()
    mock_pyautogui.screenshot.return_value = np.zeros((100, 100, 3))

    with (
        patch.object(image_instance, "get_image_path", return_value="test.png"),
        patch("programatic_x.Image.cv2.cvtColor", side_effect=lambda image, _: image),
        patch(
            "programatic_x.Image.cv2.imread",
            return_value=np.zeros((20, 40, 3)),
        ),
        patch(
            "programatic_x.Image.cv2.matchTemplate",
            return_value=np.array([[0.5, 0.1], [0.1, 0.6]]),
        ),
    ):
        with pytest.raises(pyautogui.ImageNotFoundException):
            image_instance.get_center("test.png", confidence=0.75)