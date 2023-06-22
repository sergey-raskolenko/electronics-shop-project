import pytest
from src.item import Item
from src.phone import Phone
@pytest.fixture
def item():
	item = Item("Смартфон", 10000, 20)
	return item

@pytest.fixture
def item2():
	item2 = Item("Смартфон 2", 15000, 10)
	return item2

@pytest.fixture()
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone

@pytest.fixture()
def phone2():
    phone2 = Phone("iPhone 13", 100_000, 10, 1)
    return phone2