"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

def test_instantiate_from_csv():
	Item.instantiate_from_csv()
	assert  len(Item.all) == 5


def test_string_to_number():
	assert Item.string_to_number('5') == 5
	assert Item.string_to_number('5.0') == 5
	assert Item.string_to_number('5.5') == 5

@pytest.fixture
def item():
	item = Item("Смартфон", 10000, 20)
	return item


def test__init__(item):
	"""
	Проверка принадлежности экземляра класса к классу
	"""
	assert isinstance(item, Item)
	assert item.name == "Смартфон"
	assert item.price == 10000
	assert item.quantity == 20


def test_repr__(item):
	assert repr(item) == "Item('Смартфон', 10000, 20)"


def test__str__(item):
	assert str(item) == 'Смартфон'


def test_calculate_total_price(item):
	"""
	Проверка подсчета общей стоимости продукта
	"""
	assert item.calculate_total_price() == 200_000


def test_apply_discount(item):
	"""
	Проверка применнеия скидки к определенному товару
	"""
	Item.pay_rate = 0.8
	item.apply_discount()
	assert item.price == 8000

def test_name_setter(item):
	assert item.name == "Смартфон"
	item.name = "Диктофон"
	assert item.name == "Диктофон"

def test_long_name_setter(item):
	with pytest.raises(Exception):
		item.name = "Диктофонфон"


