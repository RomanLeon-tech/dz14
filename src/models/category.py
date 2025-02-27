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
        return "\n".join(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
                         for p in self._products)
