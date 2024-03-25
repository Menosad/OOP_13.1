import pytest
import src.classes


@pytest.fixture
def categ1():
    return src.classes.Category('fruit', 'фрукты', [])


@pytest.fixture
def prod1():
    return src.classes.Product('apple', 'fruit', 50, 10)


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


@pytest.fixture
def prod6():
    return src.classes.Product('nokia 3110', 'indestructible', 100_000, 1)


def test_init_category(categ1):
    assert categ1.name == 'fruit'
    assert categ1.description == 'фрукты'
    assert categ1.number_categories == 1


def test_category_list(categ2, prod2, prod3, prod4, prod6):
    assert categ2.products == [prod2, prod3, prod4]
    categ2.products = prod6
    assert categ2.products == [prod2, prod3, prod4, prod6]


def test_add_product(categ2, prod1):
    categ2.products = prod1
    assert categ2.number_products == 4


def test_add_product2(categ2, prod5, prod6):
    categ2.products = prod5
    assert categ2.products[1].price == 20_000
    assert categ2.products[1].quantity == 10
    categ2.products = prod6
    assert categ2.products[3].name == 'nokia 3110'
    assert categ2.products[3].quantity == 1


def test_new_product(categ2):
    animal1 = src.classes.Product.new_product('fox_chibi', 'animal', 150, 1)
    assert animal1.name == 'fox_chibi'
    src.classes.Product.new_product('nokia_3110', 'indestructible', 110_000, 1, categ2)
    assert categ2.products[3].name == 'nokia_3110'
    assert categ2.products[3].price == 110_000
    assert categ2.products[3].quantity == 1
    assert categ2.number_products == 13
    src.classes.Product.new_product('xiaomi', 'chip smartphone', 25_000, 6, categ2)
    assert categ2.products[1].price == 25_000
    assert categ2.products[1].quantity == 11


def test_get_products_list(categ2):
    categ2.product_list
    assert '''samsung, 15000 руб. Остаток: 3 шт.\nxiaomi, 10000 руб. Остаток: 5 шт.\niphone, 50000 руб. Остаток: 1 шт.\n'''


def test_init_product(prod1):
    assert prod1.name == 'apple'
    assert prod1.description == 'fruit'
    assert prod1.price == 50
    assert prod1.quantity == 10


def test_product_price_getter(prod4):
    assert prod4.price == 50_000
    prod4.price = 60_000
    assert prod4.price == 60_000
    prod4.price = 0
    assert "Цена указана не корректно"


def test_string_repr_product(prod4):
    print(prod4)
    assert 'iphone, 50_000 руб. Остаток: 1 шт.'


def test_string_repr_category(categ1, categ2):
    print(categ1)
    assert 'fruit, количество продуктов: 1 шт.'
    print(categ2)
    assert 'fruit, количество продуктов: 2 шт.'


def test_plus_product(prod2, prod5):
    assert prod2 + prod5 == 45000 + 100_000
