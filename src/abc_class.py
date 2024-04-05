from abc import ABC, abstractmethod


class ABCProduct(ABC):

    @abstractmethod
    def price(self):
        pass


class AbstractOrder(ABC):

    @abstractmethod
    def products(self):
        pass

