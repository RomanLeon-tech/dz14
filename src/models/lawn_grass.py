from src.models.product import Product


class LawnGrass(Product):
    """
    Класс, представляющий траву газонную.

    :param name: Название травы.
    :param description: Описание травы.
    :param price: Цена травы.
    :param quantity: Количество травы на складе.
    :param country: Страна-производитель травы.
    :param germination_period: Срок прорастания травы.
    :param color: Цвет травы.
    """
    def __init__(self, name: str, description: str, price: float,
                 quantity: int, country: str,
                 germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
