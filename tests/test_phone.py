from src.item import Item
from src.phone import Phone
import pytest

def test__init__(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2
def test_zero_or_less_sims(phone):
    with pytest.raises(ValueError):
        phone1 = Phone("iPhone 14", 120_000, 5, 0)
    with pytest.raises(ValueError):
        phone.number_of_sim = -1

def test__repr_and__str__(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert str(phone) == 'iPhone 14'

def test__add__(item, phone, phone2):
	assert phone + phone2 == 15
	assert item + phone2 == 30
	with pytest.raises(ValueError):
		phone + 1
