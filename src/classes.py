class Category:
    """Класс принимающий на вход название категории её описание
     содержит в себе список объектов попадающих в эту категорию"""
    name: str
    description: str
    products: list

    number_categories = 0
    number_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.number_categories += 1
        Category.number_products += len(self.products)

    def add_product(self, obj: object):
        self.products.append(obj)
        Category.number_products += len(self.products)

class Product:
    """Класс принимающий на вход название, описание товара, цену
    и количество в наличии"""
    name: str
    description: str
    price: float
    quantity: int
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
