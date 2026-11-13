import pytest
from unittest.mock import patch, MagicMock
from programatic_x.Image import Image

def test_get_center_success(mock_pyautogui):
    mock_pyautogui.locateOnScreen.return_value = MagicMock()
    mock_pyautogui.center.return_value = (100, 200)
    result = Image.get_center("test.png")
    assert result == (100, 200)

def test_get_center_not_found(mock_pyautogui):
    mock_pyautogui.locateOnScreen.return_value = None
    with pytest.raises(Exception):
        Image.get_center("test.png")