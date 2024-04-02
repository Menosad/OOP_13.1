from src.classes import Product, Category
from mixin_class import MixinRepr


class Smartphone(MixinRepr, Product):
    performance: float
    model: str
    memory: str
    color: str

    smartphones = Category('smartphone', 'смартфоны, коммуникаторы', [])

    def __init__(self, name, description, __price, quantity,
                 performance: float, model: str, memory: str, color: str):
        super().__init__(name, description, __price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

        Smartphone.smartphones.products = self

    def __add__(self, other):
        if issubclass(other.__class__, Smartphone):
            self_price = self.price
            other_price = other.price
            self_summ = self.quantity * self_price
            other_summ = other.quantity * other_price
            return self_summ + other_summ
        else:
            return TypeError


sm1 = Smartphone('Apple', 'best', 60_000, 2, 4,
                 'Iphone500', '10 Tb', 'white')

sm2 = Smartphone('Samsung', 'norm', 32_000, 5, 3.7,
                      'Galaxy', '5 Tb', 'black')

print(Category.number_products)

smart1 = Smartphone('Samsung', 'norm', 32_000, 5, 3.7,
                      'Galaxy', '5 Tb', 'black')

print(repr(smart1))

