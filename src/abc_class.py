from abc import ABC, abstractmethod


class ABCProduct(ABC):

    @abstractmethod
    def price(self):
        pass
    