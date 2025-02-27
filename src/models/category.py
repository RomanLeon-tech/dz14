from typing import List
from src.models.product import Product

class Category:
    """
    Класс, представляющий категорию продуктов.

    :param name: Название категории.
    :param description: Описание категории.
    :param products: Список продуктов категории.
    """
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_products += len(products)