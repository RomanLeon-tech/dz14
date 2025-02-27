class Product:
    """
    Класс, представляющий продукт.

    :param name: Название продукта.
    :param description: Описание продукта.
    :param price: Цена продукта.
    :param quantity: Количество продукта на складе.
    """
    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict):
        return cls(
            name=product_dict['name'],
            description=product_dict['description'],
            price=product_dict['price'],
            quantity=product_dict['quantity']
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value
