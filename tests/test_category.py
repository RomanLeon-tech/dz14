import pytest
from src.models.category import Category
from src.models.product import Product


def test_category_initialization():
    product1 = Product(name="Product 1", description="Description 1", price=10.0, quantity=10)
    product2 = Product(name="Product 2", description="Description 2", price=20.0, quantity=20)
    category = Category(name="Test Category", description="This is a test category", products=[product1, product2])
    assert category.name == "Test Category"
    assert category.description == "This is a test category"
    assert len(category.products) == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2


def test_multiple_categories():
    product1 = Product(name="Product 1", description="Description 1", price=10.0, quantity=10)
    product2 = Product(name="Product 2", description="Description 2", price=20.0, quantity=20)
    category1 = Category(name="Category 1", description="Description 1", products=[product1])
    category2 = Category(name="Category 2", description="Description 2", products=[product2])
    assert Category.total_categories == 2
    assert Category.total_products == 2
