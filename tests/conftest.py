import pytest

from src.class_product import Product
from src.class_category import Category


@pytest.fixture
def product_iphone():   # Фикстура для проверки инициализации класса Product
    return Product("Iphone 15", "512 GB, Gray space", 210000.0, 8)