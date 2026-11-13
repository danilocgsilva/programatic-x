import pytest
from unittest.mock import patch
from programatic_x.factory.ButtonStartFactory import ButtonStartFactory
from programatic_x.WindowsButtonStart import WindowsButtonStart
from programatic_x.MainStartKey import MainStartKey

def test_create_windows_button_start(mock_platform_windows):
    button = ButtonStartFactory.create_button_start()
    assert isinstance(button, WindowsButtonStart)
    assert True

def test_create_linux_button_start(mock_platform_linux):
    button = ButtonStartFactory.create_button_start()
    assert isinstance(button, MainStartKey)

@patch('programatic_x.factory.ButtonStartFactory.platform')
def test_create_default_button_start(mock_system):
    mock_system.return_value = "Linux"
    button = ButtonStartFactory.create_button_start()
    assert isinstance(button, MainStartKey)