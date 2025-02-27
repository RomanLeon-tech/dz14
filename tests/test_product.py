import pytest
from src.models.product import Product


def test_product_initialization():
    product = Product(name="Test Product", description="This is a test product", price=100.0, quantity=5)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 100.0
    assert product.quantity == 5
