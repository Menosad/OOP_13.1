from abc import ABC, abstractmethod


class ABCProduct(ABC):
    """Абстрактный класс - шаблон для создания классов продуктов"""

    @abstractmethod
    def new_product(self, name, description, price, quantity, cat_obj=None):
        pass
