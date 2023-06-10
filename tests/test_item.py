"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

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
