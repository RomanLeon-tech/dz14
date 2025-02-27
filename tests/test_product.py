from src.models.product import Product


def test_product_initialization():
    product = Product(name="Test Product",
                      description="This is a test product",
                      price=100.0, quantity=5)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 100.0
    assert product.quantity == 5


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
