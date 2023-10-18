"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone


def test_instance_item():
    item = Item(name='Device', price=99.9, quantity=10)
    assert item.name == 'Device'
    assert item.price == 99.9
    assert item.quantity == 10


def test_calculate_price():
    item = Item(name='Device', price=99.9, quantity=10)
    assert item.calculate_total_price() == 999.0


def test_class_param():
    item = Item(name='Device', price=99.9, quantity=10)
    assert item.pay_rate == 1.0
    assert Item.pay_rate == 1.0
    Item.pay_rate = 1.5
    assert item.pay_rate == 1.5
    assert Item.pay_rate == 1.5


def test_apply_discount():
    item = Item(name='Device', price=99.9, quantity=10)
    assert item.price == 99.9
    Item.pay_rate = 1.5
    assert item.apply_discount() is None
    assert item.price == 149.85


def test_name():
    item = Item(name='Device', price=10.0, quantity=5)
    item.name = 'Smart2'
    assert item.name == 'Smart2'
    item.name = 'SmartPhone10'
    assert item.name == 'SmartPhone'


def test_create_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_convert_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_representation():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_phone():
    item = Item('CDcard', 1000, 100)
    phone = Phone('Honor20', 30000, 10, 2)
    assert repr(item) == "Item('CDcard', 1000, 100)"
    assert repr(phone) == "Phone('Honor20', 30000, 10, 2)"
    assert phone.number_of_sim == 2


def test_phone_sum():
    item = Item('CDcard', 1000, 100)
    phone1 = Phone('Honor20', 30000, 10, 2)
    phone2 = Phone('GalaxyS10', 60000, 6, 2)
    assert item + item == 200
    assert item + phone1 == 110
    assert phone1 + phone2 == 16
    item_int = int(10)
    assert phone1 + item_int == 10


def test_sims():
    phone1 = Phone('Honor20', 30000, 10, 2)
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
