import pytest

from src.class_product import Product
from src.class_category import Category


@pytest.fixture
def product_iphone():
    """Фикстура для проверки инициализации класса Product."""

    return Product("Iphone 15", "512 GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_phone():
    """Фикстура для проверки инициализации класса Category."""

    product_1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category_1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        [product_1, product_2, product_3],
    )

    return category_1


@pytest.fixture
def category_tv():
    """Фикстура для проверки счетчиков категорий
    и продуктов класса Category."""

    product_4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category_2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [product_4],
    )

    return category_2


@pytest.fixture
def category_with_empty_products():
    """Фикстура с объектом класса Category с пустым списком продуктов для проверки
    метода add_product."""

    category_1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        [],
    )
    return category_1


@pytest.fixture
def check_add_product():
    """Фикстура для проверки метода add_product в классе Category."""

    product_4 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    return product_4
