from abc import ABC
from abc_class import AbstractOrder


class Order(AbstractOrder, ABC):

    def __init__(self, prod, name: str, description: str, price: int, quantity: int):
        super().__init__(name, description, price, quantity)

        ...

    pass
