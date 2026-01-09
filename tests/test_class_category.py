import pytest

from src.class_category import Category
from src.class_product import Product


def test_init_category_and_count_attribute(category_phone, category_tv):
    """Тестирование инициализации и счетчиков класса Category."""

    assert category_phone.name == "Смартфоны"
    assert category_phone.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_phone._Category__products) == 3
    assert category_tv.name == "Телевизоры"
    assert category_tv.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )
    assert len(category_tv._Category__products) == 1
    assert category_phone.product_count == 4
    assert category_phone.category_count == 2
    assert category_tv.product_count == 4
    assert category_tv.category_count == 2


def test_add_product(category_with_empty_products, check_add_product):
    """Тест для проверки метода add_product в классе Category."""

    category_with_empty_products.add_product(check_add_product)
    assert len(category_with_empty_products._Category__products) == 1
    assert category_with_empty_products.product_count == 5


def test_add_product_existing_product():
    """Тест для проверки метода add_product, в случае, когда продукт уже существует в списке."""

    category = Category("Смартфоны", "Для жизни и связи")
    product_1 = Product("Iphone 15", "Телефон", 120000.0, 5)
    product_2 = Product("Iphone 15", "Телефон", 130000.0, 2)

    category.add_product(product_1)
    category.add_product(product_2)

    products = category._Category__products
    assert len(products) == 1
    assert products[0].quantity == 7
    assert products[0].price == 130000.0


def test_add_product_smartphone_and_lawngrass(
    object_smartphone, object_lawngrass
):
    """Тест для проверки добавления продуктов из подклассов Smartphone и LawnGrass."""

    category_1 = Category("Смартфоны", "Для жизни и связи")
    category_1.add_product(object_lawngrass)
    category_1.add_product(object_smartphone)
    products = category_1._Category__products
    assert len(products) == 2


def test_add_product_error():
    """Тест для проверки невозможности добавления в список продуктов класса Category иных объектов,
    отличных от класса Product и его подклассов."""

    category_2 = Category("Смартфоны", "Для жизни и связи")
    products = ["Iphone", "Samsung", "Nokia"]

    with pytest.raises(TypeError):
        category_2.add_product(products)


def test_products_category(category_phone):
    """Тест для проверки геттера products в классе Category."""

    assert category_phone.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        "\nIphone 15, 210000.0 руб. Остаток: 8 шт."
        "\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_str_category(category_phone):
    """Тест для проверки магического метода __str__ в классе Category."""

    assert str(category_phone) == "Смартфоны, количество продуктов: 27 шт."


def test_middle_price_category(category_phone):
    """Тест на проверку метода middle_price класса Category в случае наличия товаров."""

    assert category_phone.middle_price() == 140333.33333333334


def test_empty_product_middle_price_category(category_with_empty_products):
    """Тест метода middle_price класса Category при отсутствии продуктов."""

    assert category_with_empty_products.middle_price() == 0
