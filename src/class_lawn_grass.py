from src.classes import Product, Category
from src.mixin_class import MixinRepr


class LawnGrass(Product, MixinRepr):
    """Класс газонная трава"""
    country_of_origin: str
    germination_period: int
    color: str

    # объект класса Category, создается при инициализации объекта класса с травой
    lawngrass = Category('grass', 'lawn grass', [])

    def __init__(self, name, description, price, quantity, country_of_origin: str,
                 germination_period: int, color: str):
        # вызов метода __init__ у родительского класса, для инициализации общих аргументов
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
        # добавления продукта в список продуктов созданной категории
        LawnGrass.lawngrass.products = self

    def __add__(self, other):
        """Метода __add__ который складывает общую стоимость двух товаров класса LawnGrass"""
        if issubclass(other.__class__, LawnGrass):
            self_price = self.price
            other_price = other.price
            self_summ = self.quantity * self_price
            other_summ = other.quantity * other_price
            return self_summ + other_summ
        else:
            return TypeError


gras1 = LawnGrass('Russian grass', 'good grass', 500, 1000, 'Russian',
                  2, 'green')
