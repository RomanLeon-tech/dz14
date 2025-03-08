import pytest
from src.models.product import Product
from src.models.smartphone import Smartphone
from src.models.lawn_grass import LawnGrass


def test_product_initialization():
    product = Product(name="Test Product",
                      description="This is a test product",
                      price=100.0, quantity=5)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 100.0
    assert product.quantity == 5


def test_product_initialization_zero_quantity():
    with pytest.raises(ValueError,
                       match="Товар с нулевым количеством "
                             "не может быть добавлен"):
        Product(name="Test Product",
                description="This is a test product",
                price=100.0, quantity=0)


def test_product_price_setter():
    product = Product(name="Test Product",
                      description="This is a test product",
                      price=100.0, quantity=5)
    product.price = 200.0
    assert product.price == 200.0
    product.price = -10.0
    assert product.price == 200.0


def test_new_product():
    product_dict = {
        "name": "New Product",
        "description": "This is a new product",
        "price": 150.0,
        "quantity": 10
    }
    product = Product.new_product(product_dict)
    assert product.name == "New Product"
    assert product.description == "This is a new product"
    assert product.price == 150.0
    assert product.quantity == 10


def test_product_str():
    product = Product(name="Test Product",
                      description="This is a test product",
                      price=100.0, quantity=5)
    assert str(product) == ("Test Product, 100.0 руб. "
                            "Остаток: 5 шт.")


def test_product_addition():
    product1 = Product(name="Product 1",
                       description="Description 1",
                       price=10.0, quantity=10)
    product2 = Product(name="Product 2",
                       description="Description 2",
                       price=20.0, quantity=2)
    assert product1 + product2 == 140.0


def test_smartphone_initialization():
    smartphone = Smartphone(name="Smartphone 1",
                            description="Description 1",
                            price=500.0, quantity=10,
                            efficiency="High",
                            model="Model X", memory=128,
                            color="Black")
    assert smartphone.name == "Smartphone 1"
    assert smartphone.description == "Description 1"
    assert smartphone.price == 500.0
    assert smartphone.quantity == 10
    assert smartphone.efficiency == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == 128
    assert smartphone.color == "Black"


def test_lawn_grass_initialization():
    lawn_grass = LawnGrass(name="Lawn Grass 1",
                           description="Description 1",
                           price=50.0, quantity=100,
                            country="USA",
                           germination_period=30, color="Green")
    assert lawn_grass.name == "Lawn Grass 1"
    assert lawn_grass.description == "Description 1"
    assert lawn_grass.price == 50.0
    assert lawn_grass.quantity == 100
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == 30
    assert lawn_grass.color == "Green"


def test_product_addition_type_error():
    smartphone = Smartphone(name="Smartphone 1",
                            description="Description 1",
                            price=500.0, quantity=10,
                            efficiency="High",
                            model="Model X", memory=128,
                            color="Black")
    lawn_grass = LawnGrass(name="Lawn Grass 1",
                           description="Description 1",
                           price=50.0, quantity=100,
                            country="USA",
                           germination_period=30, color="Green")
    with pytest.raises(TypeError):
        smartphone + lawn_grass
