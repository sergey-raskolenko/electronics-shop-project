from src.keyboard import KeyBoard, KeyboardLanguages
from src.item import Item
import pytest

def test__init__():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert isinstance(kb, KeyBoard)
    assert isinstance(kb, KeyboardLanguages)
    assert isinstance(kb, Item)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang().change_lang()
    assert kb.language == "RU"
    with pytest.raises(AttributeError):
        kb.language = "CN"
