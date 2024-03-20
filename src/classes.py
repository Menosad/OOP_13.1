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
        self._products = products

        Category.number_categories += 1
        Category.number_products += len(self._products)

    def add_product(self, prod):
        repetitions = 0
        for obj in self._products:
            if obj.name == prod.name:
                if obj.price < prod.price:
                    obj.price = prod.price
                obj.quantity += prod.quantity
                repetitions += 1
        if repetitions == len(self._products):
            self._products.append(prod)
            Category.number_products += 1

    @property
    def get_product_list(self):
        """Получение списка продуктов с указанием каждого продукта
        на отдельной строке"""
        str_line = ''
        for obj in self._products:
            str_line += f"{obj.name}, {obj.price} руб. Остаток: {obj.quantity} шт.\n"
        return str_line


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

    @classmethod
    def from_string(cls, new_str):
        """Метод создающий объект класса из строки:
        название-описание-цена-количество"""
        name, description, price, quantity = new_str.split('-')
        return cls(name, description, price, quantity)

    @property
    def get_price(self):
        return self.price

    @get_price.setter
    def get_price(self, price: int):
        if int(price) > 0:
            self.price = int(price)
        else:
            print(f"Цена указана не корректно")