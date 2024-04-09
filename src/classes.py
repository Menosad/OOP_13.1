from src.mixin_class import MixinRepr
from src.abc_class import ABCProduct


class Category:
    """Класс принимающий на вход название категории её описание
     содержит в себе список объектов попадающих в эту категорию"""

    name: str
    description: str
    products: list

    number_categories = 0
    number_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.number_categories += 1
        Category.number_products += len(self.__products)

    def __len__(self):
        return sum(obj.quantity for obj in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    @property
    def products(self):
        """Геттер возвращает список продуктов"""
        return self.__products

    def avg_price(self):
        """Метод подсчета среднего ценника по Категории"""
        try:
            amount_sum = sum(obj.price * obj.quantity for obj in self.__products)
            result_amount = amount_sum / len(self)
            return round(result_amount, 2)
        except ZeroDivisionError:
            return 0

    @products.setter
    def products(self, prod):
        """Добавляет продукт в список продуктов, если такой продукт уже есть в списке
        и цена нового продукта выше, то устанавливается цена нового продукта
        :объект.products = объект"""
        if issubclass(prod.__class__, Product):
            for obj in self.__products:
                if obj.name == prod.name:
                    if obj.price < prod.price:
                        obj.price = prod.price
                    obj.quantity += prod.quantity
                    return
            if prod.quantity == 0:
                raise ValueError('Товар с нулевым количеством не может быть добавлен')
            self.__products.append(prod)
            Category.number_products += 1
        else:
            raise TypeError('Класс добавляемого объекта не входит в семейтво классов Product')

    @property
    def product_list(self):
        """Получение списка продуктов с указанием каждого продукта
        на отдельной строке"""
        line = ''
        for obj in self.__products:
            obj_str = f"{obj}"
            line += obj_str + '\n'
        return line


class Product(MixinRepr, ABCProduct):
    """Класс принимающий на вход название, описание товара, цену
    и количество в наличии"""

    def __init__(self, name: str, description: str, price: int, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()


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

