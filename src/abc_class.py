from abc import ABC, abstractmethod


class ABCProduct(ABC):

    @abstractmethod
    def new_product(self):
        pass


class AbstractOrder(ABC):

    @abstractmethod
    def products(self):
        pass

