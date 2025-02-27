from typing import Iterator
from src.models.category import Category
from src.models.product import Product


class IterableCategory:
    """
    Вспомогательный класс для итерации по товарам категории.

    :param category: Объект класса Category.
    """
    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self) -> Iterator[Product]:
        return self

    def __next__(self) -> Product:
        if self.index < len(self.category._products):
            product = self.category._products[self.index]
            self.index += 1
            return product
        raise StopIteration
