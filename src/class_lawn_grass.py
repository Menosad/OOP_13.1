from classes import Category

class LawnGrass(Category):

    def __init__(self, name, description: str, products: list, country_of_origin: str,
                 germination_period: int, color: str):
        super().__init__(name, description, products)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
