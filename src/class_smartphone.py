from classes import Category


class Smartphone(Category):

    def __init__(self, name, description, products, performance, model,
                 memory, color):
        super().__init__(name, description, products)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
