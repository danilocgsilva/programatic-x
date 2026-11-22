from unittest.mock import MagicMock, call, patch
from programatic_x.LongType import LongType


@patch("programatic_x.LongType.sleep")
@patch("programatic_x.LongType.Controller")
def test_type_calls_keyboard_type(mock_controller, mock_sleep):
    keyboard = MagicMock()
    mock_controller.return_value = keyboard

    LongType().type("hello world")

    assert keyboard.type.call_args_list == [call(character) for character in "hello world"]


@patch("programatic_x.LongType.sleep")
@patch("programatic_x.LongType.Controller")
def test_type_passes_empty_string(mock_controller, mock_sleep):
    keyboard = MagicMock()
    mock_controller.return_value = keyboard

    LongType().type("")

    keyboard.type.assert_not_called()


@patch("programatic_x.LongType.sleep")
@patch("programatic_x.LongType.Controller")
def test_type_passes_special_characters(mock_controller, mock_sleep):
    keyboard = MagicMock()
    mock_controller.return_value = keyboard
    text = "Hello, World! 123 @#$"

    LongType().type(text)

    assert keyboard.type.call_args_list == [call(character) for character in text]


@patch("programatic_x.LongType.sleep")
@patch("programatic_x.LongType.Controller")
def test_type_calls_keyboard_exactly_once_per_character(mock_controller, mock_sleep):
    keyboard = MagicMock()
    mock_controller.return_value = keyboard
    long_type = LongType()

    long_type.type("first")
    long_type.type("second")

    assert keyboard.type.call_count == len("first") + len("second")
