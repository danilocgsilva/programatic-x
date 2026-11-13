import pytest
from unittest.mock import patch, MagicMock
from programatic_x.WindowsButtonStart import WindowsButtonStart
from programatic_x.exceptions.CouldNotLocateStartButton import CouldNotLocateStartButton

def test_click_success_first_image(mock_pyautogui):
    mock_pyautogui.locateOnScreen.return_value = MagicMock()
    instance = WindowsButtonStart()
    instance.click()
    assert mock_pyautogui.click.called

def test_click_success_second_image(mock_pyautogui):
    mock_pyautogui.locateOnScreen.side_effect = [None, MagicMock(), None]
    instance = WindowsButtonStart()
    instance.click()
    assert mock_pyautogui.click.called

def test_click_all_images_fail(mock_pyautogui):
    mock_pyautogui.locateOnScreen.return_value = None
    instance = WindowsButtonStart()
    with pytest.raises(CouldNotLocateStartButton):
        instance.click()