from src.classes import  Product


class Smartphone(Product):
    performance: float
    model: str
    memory: str
    color: str

    def __init__(self, name, description, price, quantity,
                 performance: float, model: str, memory: str, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
