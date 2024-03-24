class Category:
    """Класс принимающий на вход название категории её описание
     содержит в себе список объектов попадающих в эту категорию"""

    number_categories = 0
    number_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.number_categories += 1
        Category.number_products += len(self.__products)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, prod):
        for obj in self.__products:
            if obj.name == prod.name:
                if obj.price < prod.price:
                    obj.price = prod.price
                obj.quantity += prod.quantity
                return
        self.__products.append(prod)
        Category.number_products += 1

    @property
    def product_list(self):
        """Получение списка продуктов с указанием каждого продукта
        на отдельной строке"""
        str_line = ''
        for obj in self.__products:
            str_line += f"{obj.name}, {obj.price} руб. Остаток: {obj.quantity} шт.\n"
        return str_line


class Product:
    """Класс принимающий на вход название, описание товара, цену
    и количество в наличии"""

    def __init__(self, name: str, description: str, price: int, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity, categ_obj=None):
        """Метод создающий объект класса"""
        prod = cls(name, description, price, quantity)
        if categ_obj is None:
            return prod
        else:
            categ_obj.products = prod
        return prod

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @price.setter
    def price(self, value):
        if value > self.__price:
            self.__price = value
        elif value <= 0:
            print('Цена указана не корректно')
