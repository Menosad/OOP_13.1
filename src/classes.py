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

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

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
        for obj in self.__products:
            print(obj)


class Product:
    """Класс принимающий на вход название, описание товара, цену
    и количество в наличии"""

    def __init__(self, name: str, description: str, price: int, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.name} ('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        self_summ = self.quantity * self.__price
        other_summ = other.quantity * other.__price
        return self_summ + other_summ

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


class New_Class:

    def __init__(self, category, stop):
        self.category = category
        self.stop = stop

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < self.stop:
            self.current_value += 1
            return self.category.__products[self.current_value]
        else:
            raise StopIteration
