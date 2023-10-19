import pytest
from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_keyboard_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

    # AttributeError: property 'language' of 'Keyboard' object has no setter
    with pytest.raises(AttributeError):
        kb.language = 'CH'
