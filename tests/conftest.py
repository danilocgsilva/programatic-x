import pytest
from unittest.mock import patch, MagicMock
from programatic_x.factory.ButtonStartFactory import ButtonStartFactory
from programatic_x.WindowsButtonStart import WindowsButtonStart
from programatic_x.MainStartKey import MainStartKey

@pytest.fixture(autouse=True)
def mock_pyautogui():
    with patch('programatic_x.Image.pyautogui') as mock_pyautogui:
        mock_pyautogui.locateOnScreen.return_value = None
        mock_pyautogui.center.return_value = (500, 500)
        yield mock_pyautogui

@pytest.fixture(autouse=True)
def mock_subprocess():
    with patch('programatic_x.MainStartKey.subprocess') as mock_subprocess:
        mock_subprocess.run.return_value = MagicMock()
        yield mock_subprocess

@pytest.fixture
def mock_platform_windows():
    with patch('programatic_x.factory.ButtonStartFactory.platform.system') as mock_system:
        mock_system.return_value = "Windows"
        yield mock_system

@pytest.fixture
def mock_platform_linux():
    with patch('programatic_x.factory.ButtonStartFactory.platform.system') as mock_system:
        mock_system.return_value = "Linux"
        yield mock_system