from src.phone import Phone
from src.item import Item
import pytest


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
