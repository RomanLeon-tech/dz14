from src.models import Product, Category


def test_product_initialization():
    product = Product("Test Product", "This is a test product", 100.0, 5)
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 100.0
    assert product.quantity == 5


def test_category_initialization():
    category = Category("Test Category", "This is a test category")
    assert category.name == "Test Category"
    assert category.description == "This is a test category"
    assert category.products == []
    assert Category.category_count == 1


def test_add_product_to_category():
    category = Category("Test Category", "This is a test category")
    product = Product("Test Product", "This is a test product", 100.0, 5)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product
    assert Category.product_count == 1


def test_total_categories_and_products():
    category1 = Category("Category 1", "Description 1")
    category2 = Category("Category 2", "Description 2")
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 10)
    category1.add_product(product1)
    category2.add_product(product2)
    assert Category.category_count == 2
    assert Category.product_count == 2
