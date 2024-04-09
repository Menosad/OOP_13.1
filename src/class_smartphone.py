from src.classes import Product, Category


class Smartphone(Product):
    """Класс для создания продуктов различных смартфонов"""
    performance: float
    model: str
    memory: str
    color: str

    smartphones = Category('smartphone', 'смартфоны, коммуникаторы', [])

    def __init__(self, name, description, __price, quantity,
                 performance: float, model: str, memory: str, color: str):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, __price, quantity)

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
