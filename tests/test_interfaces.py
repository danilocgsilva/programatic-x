import pytest
from programatic_x.interfaces.ButtonStartInterface import ButtonStartInterface
from programatic_x.WindowsButtonStart import WindowsButtonStart
from programatic_x.MainStartKey import MainStartKey

def test_button_start_interface_is_abstract():
    with pytest.raises(TypeError):
        ButtonStartInterface()

def test_windows_button_start_implements_interface():
    assert issubclass(WindowsButtonStart, ButtonStartInterface)

def test_main_start_key_implements_interface():
    assert issubclass(MainStartKey, ButtonStartInterface)