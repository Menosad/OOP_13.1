from classes import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity,
                 performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
