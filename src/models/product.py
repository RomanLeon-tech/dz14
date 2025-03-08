from src.models.base_product import BaseProduct
from src.models.mixins import LoggerMixin


class Product(LoggerMixin, BaseProduct):
    """
    Класс, представляющий продукт.

    :param name: Название продукта.
    :param description: Описание продукта.
    :param price: Цена продукта.
    :param quantity: Количество продукта на складе.
    """
    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством"
                             " не может быть добавлен")
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть "
                  "нулевая или отрицательная")
        else:
            self._price = value

    def __str__(self):
        return (f"{self.name}, {self.price} руб. "
                f"Остаток: {self.quantity} шт.")

    def __add__(self, other):
        if isinstance(other, Product) and type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операнд должен быть экземпляром того же класса")
