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
        if isinstance(product, Product):
            self._products.append(product)
            Category.total_products += 1
        else:
            raise TypeError("Можно добавлять только объекты "
                            "класса Product или его наследников")

    @property
    def products(self):
        return "\n".join(str(p) for p in self._products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def average_price(self):
        if not self._products:
            return 0
        total_price = sum(p.price for p in self._products)
        return total_price / len(self._products)
