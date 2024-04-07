import pytest

from src.class_lawn_grass import LawnGrass


@pytest.fixture
def grass1():
    return LawnGrass('Russian grass', 'good grass', 500, 1000, 'Russian',
                     2, 'green')


@pytest.fixture
def grass2():
    return LawnGrass('France grass', 'not good grass', 12_000, 100, 'France',
                     5, 'brown')


@pytest.fixture
def test():
    class TestClass:
        pass

    return TestClass()


def test_init_lawn_grass(grass):
    assert grass.name == 'Russian grass'


def test_add_wrong_class(grass1, test):
    print(grass1 + test)
    assert TypeError


def test_add_wrong_type_object(test, grass1):
    LawnGrass.lawngrass = test
    assert TypeError
