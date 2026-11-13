import pytest
from unittest.mock import patch
from programatic_x.LongType import LongType


@patch("programatic_x.LongType.pyautogui")
def test_type_calls_pyautogui_write(mock_pyautogui):
    LongType().type("hello world")

    mock_pyautogui.write.assert_called_once_with("hello world")


@patch("programatic_x.LongType.pyautogui")
def test_type_passes_empty_string(mock_pyautogui):
    LongType().type("")

    mock_pyautogui.write.assert_called_once_with("")


@patch("programatic_x.LongType.pyautogui")
def test_type_passes_special_characters(mock_pyautogui):
    LongType().type("Hello, World! 123 @#$")

    mock_pyautogui.write.assert_called_once_with("Hello, World! 123 @#$")


@patch("programatic_x.LongType.pyautogui")
def test_type_calls_write_exactly_once_per_call(mock_pyautogui):
    long_type = LongType()
    long_type.type("first")
    long_type.type("second")

    assert mock_pyautogui.write.call_count == 2
