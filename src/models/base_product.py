from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Базовый абстрактный класс для продуктов.
    """

    @abstractmethod
    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
