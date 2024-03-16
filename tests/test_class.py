import pytest
import src.clases


@pytest.fixture
def categ1():
    return src.clases.Category('fruit', 'фрукты')


@pytest.fixture
def prod1():
    return src.clases.Product('apple', 'fruit',
                              50, 10)


def test_init_category(categ1):
    assert categ1.name == 'fruit'
    assert categ1.description == 'фрукты'
    assert categ1.number_categoryes == 1


def test_add_product(categ1, prod1):
    categ1.add_product(prod1)
    assert categ1.numbers_products() == 1


def test_init_product(prod1):
    assert prod1.name == 'apple'
    assert prod1.description == 'fruit'
    assert prod1.price == 50
    assert prod1.quantity == 10
