from classes import Product


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country_of_origin: str,
                 germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
