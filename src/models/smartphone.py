from src.models.product import Product


class Smartphone(Product):
    """
    Класс, представляющий смартфон.

    :param name: Название смартфона.
    :param description: Описание смартфона.
    :param price: Цена смартфона.
    :param quantity: Количество смартфонов на складе.
    :param efficiency: Производительность смартфона.
    :param model: Модель смартфона.
    :param memory: Объем встроенной памяти смартфона.
    :param color: Цвет смартфона.
    """
    def __init__(self, name: str, description: str,
                 price: float, quantity: int,
                 efficiency: str, model: str,
                 memory: int, color: str):
        super().__init__(name, description,
                         price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
