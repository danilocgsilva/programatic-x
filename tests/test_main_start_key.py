import pytest
from unittest.mock import patch
from programatic_x.MainStartKey import MainStartKey

def test_click_keyboard_shortcut(mock_subprocess):
    instance = MainStartKey()
    instance.click()
    mock_subprocess.run.assert_called_once()