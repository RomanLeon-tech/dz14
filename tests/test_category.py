import pytest
from src.models.category import Category
from src.models.product import Product
from src.models.iterable_category import IterableCategory


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.total_categories = 0
    Category.total_products = 0


def test_category_initialization():
    product1 = Product(name="Product 1",
                       description="Description 1",
                       price=10.0, quantity=10)
    product2 = Product(name="Product 2",
                       description="Description 2",
                       price=20.0, quantity=20)
    category = Category(name="Test Category",
                        description="This is a test category")
    category.add_product(product1)
    category.add_product(product2)
    assert category.name == "Test Category"
    assert category.description == "This is a test category"
    assert len(category._products) == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2


def test_multiple_categories():
    product1 = Product(name="Product 1",
                       description="Description 1",
                       price=10.0, quantity=10)
    product2 = Product(name="Product 2",
                       description="Description 2",
                       price=20.0, quantity=20)
    category1 = Category(name="Category 1",
                         description="Description 1")
    category2 = Category(name="Category 2",
                         description="Description 2")
    category1.add_product(product1)
    category2.add_product(product2)
    assert Category.total_categories == 2
    assert Category.total_products == 2


def test_products_getter():
    product1 = Product(name="Product 1",
                       description="Description 1",
                       price=10.0, quantity=10)
    product2 = Product(name="Product 2",
                       description="Description 2",
                       price=20.0, quantity=20)
    category = Category(name="Test Category",
                        description="This is a test category")
    category.add_product(product1)
    category.add_product(product2)
    expected_output = ("Product 1, 10.0 руб. Остаток: "
                       "10 шт.\nProduct 2, 20.0 руб. Остаток: 20 шт.")
    assert category.products == expected_output


def test_category_str():
    product1 = Product(name="Product 1",
                       description="Description 1",
                       price=10.0, quantity=10)
    product2 = Product(name="Product 2",
                       description="Description 2",
                       price=20.0, quantity=20)
    category = Category(name="Test Category",
                        description="This is a test category")
    category.add_product(product1)
    category.add_product(product2)
    assert str(category) == ("Test Category,"
                             " количество продуктов: 30 шт.")


def test_iterable_category():
    product1 = Product(name="Product 1",
                       description="Description 1",
                       price=10.0, quantity=10)
    product2 = Product(name="Product 2",
                       description="Description 2",
                       price=20.0, quantity=20)
    category = Category(name="Test Category",
                        description="This is a test category")
    category.add_product(product1)
    category.add_product(product2)
    iterable_category = IterableCategory(category)
    products = list(iterable_category)
    assert products == [product1, product2]


def test_add_product_type_error():
    category = Category(name="Test Category",
                        description="This is a test category")
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_average_price():
    product1 = Product(name="Product 1",
                       description="Description 1",
                       price=10.0, quantity=10)
    product2 = Product(name="Product 2",
                       description="Description 2",
                       price=20.0, quantity=20)
    category = Category(name="Test Category",
                        description="This is a test category")
    category.add_product(product1)
    category.add_product(product2)
    assert category.average_price() == 15.0


def test_average_price_no_products():
    category = Category(name="Test Category",
                        description="This is a test category")
    assert category.average_price() == 0
