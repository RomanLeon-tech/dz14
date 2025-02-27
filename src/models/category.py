from src.models.product import Product


class Category:
    """
    Класс, представляющий категорию продуктов.

    :param name: Название категории.
    :param description: Описание категории.
    """
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self._products = []
        Category.total_categories += 1

    def add_product(self, product: Product):
        self._products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        return "\n".join(str(p) for p in self._products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
