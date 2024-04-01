from src.class_smartphone import Smartphone

import pytest

@pytest.fixture
def samsung():
    return Smartphone('Samsung', 'norm', 32_000, 5, 3.7,
                      'Galaxy', '5 Tb', 'black')

@pytest.fixture
def apple():
    phone2 = Smartphone('Apple', 'best', 60_000, 2, 4,
                      'Iphone500', '10 Tb', 'white')
    return phone2
    pass

def test_init(samsung):
    assert samsung.name == 'Samsung'
    assert samsung.color == 'black'

def test_add_smartphone(samsung, apple):
    assert samsung + apple == 280_000
