import pytest
from unittest.mock import patch, MagicMock, call
from pyautogui import ImageNotFoundException
from programatic_x.WindowsButtonStart import WindowsButtonStart
from programatic_x.exceptions.CouldNotLocateStartButton import CouldNotLocateStartButton


@pytest.fixture
def image_center():
    return MagicMock(name="image_center")


@patch("programatic_x.WindowsButtonStart.pyautogui.click")
@patch("programatic_x.WindowsButtonStart.Image")
def test_first_image_success_clicks_and_stops(MockImage, mock_click, image_center):
    MockImage.get_center.return_value = image_center

    WindowsButtonStart().click()

    # Tried exactly the first image
    MockImage.get_center.assert_called_once_with(
        "windows11_start_menu_100_dark.png", 0.8
    )
    # Clicked exactly the center it was given
    mock_click.assert_called_once_with(image_center)

@patch("programatic_x.WindowsButtonStart.pyautogui.click")
@patch("programatic_x.WindowsButtonStart.Image")
def test_falls_back_to_second_image(MockImage, mock_click, image_center):
    MockImage.get_center.side_effect = [
        ImageNotFoundException,
        image_center,
    ]

    WindowsButtonStart().click()

    assert MockImage.get_center.call_args_list == [
        call("windows11_start_menu_100_dark.png", 0.8),
        call("windows11_start_menu_100_light.png", 0.8),
    ]

    mock_click.assert_called_once_with(image_center)


@patch("programatic_x.WindowsButtonStart.pyautogui.click")
@patch("programatic_x.WindowsButtonStart.Image")
def test_all_images_fail_raises_and_never_clicks(MockImage, mock_click):
    MockImage.get_center.side_effect = ImageNotFoundException

    with pytest.raises(CouldNotLocateStartButton):
        WindowsButtonStart().click()

    assert MockImage.get_center.call_count == 3
    mock_click.assert_not_called()