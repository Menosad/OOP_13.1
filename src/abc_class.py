from abc import ABC, abstractmethod


class ABCProduct(ABC):

    @abstractmethod
    def new_product(self, name, description, price, quantity, cat_obj=None):
        pass


class AbstractOrder(ABC):

    @abstractmethod
    def products(self):
        pass

