import pytest
import src.classes


@pytest.fixture
def categ1():
    return src.classes.Category('fruit', 'фрукты', [])


@pytest.fixture
def prod1():
    return src.classes.Product('apple', 'fruit',
                               50, 10)


@pytest.fixture
def prod2():
    return src.classes.Product('samsung', 'smartphone', 15_000, 3)


@pytest.fixture
def prod3():
    return src.classes.Product('xiaomi', 'chip smartphone', 10_000, 5)


@pytest.fixture
def prod4():
    return src.classes.Product('iphone', 'expensive smartphone', 50_000, 1)


@pytest.fixture
def categ2(prod2, prod3, prod4):
    return src.classes.Category('mobilniki', 'mobile phones', [prod2, prod3, prod4])


@pytest.fixture
def prod5():
    return src.classes.Product('xiaomi', 'chip smartphone', 20_000, 5)


def test_init_category(categ1):
    assert categ1.name == 'fruit'
    assert categ1.description == 'фрукты'
    assert categ1.number_categories == 1


def test_add_product(categ1, prod1):
    categ1.add_product(prod1)
    assert categ1.number_products == 1


def test_add_product2(categ2, prod5):
    categ2.add_product(prod5)
    assert categ2._products[1].price == 20_000
    assert categ2._products[1].quantity == 10

def test_get_products_liost(categ2):
    assert categ2.get_product_list == '''samsung, 15000 руб. Остаток: 3 шт.\nxiaomi, 10000 руб. Остаток: 5 шт.\niphone, 50000 руб. Остаток: 1 шт.\n'''

def test_init_product(prod1):
    assert prod1.name == 'apple'
    assert prod1.description == 'fruit'
    assert prod1.price == 50
    assert prod1.quantity == 10

def test_product_price_getter(prod4):
    assert prod4.get_price == 50_000
    prod4.get_price = 60_000
    assert prod4.get_price == 60_000
    prod4.get_price = 0
    assert "Цена указана не корректно"
