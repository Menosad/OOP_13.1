from src.class_smartphone import Smartphone
import pytest

@pytest.fixture
def samsung():
    return Smartphone('Samsung', 'norm', 32_000, 5, 3.7,
                      'Galaxy', '5 Tb', 'black')


def test_init(samsung):
    assert samsung.name == 'Samsung'
    assert samsung.color == 'black'
