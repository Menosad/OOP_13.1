class Category:
    """Класс принимающий на вход название категории её описание
     содержит в себе список объектов попадающих в эту категорию"""
    number_categoryes = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

        Category.number_categoryes += 1

    def add_product(self, obj: object):
        self.products.append(obj)

    def numbers_products(self):
        return len(self.products)

class Product:
    """Класс принимающий на вход название, описание товара, цену
    и количество в наличии"""
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
