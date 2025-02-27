class Product:
    """
    Класс, представляющий продукт.

    :param name: Название продукта.
    :param description: Описание продукта.
    :param price: Цена продукта.
    :param quantity: Количество продукта на складе.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity