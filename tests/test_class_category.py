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
    """Тест для проверки метода add_product, в случае, когда продукт уже существует в списке. """

    category = Category("Смартфоны", "Для жизни и связи")
    product_1 = Product("Iphone 15", "Телефон", 120000.0, 5)
    product_2 = Product("Iphone 15", "Телефон", 130000.0, 2)

    category.add_product(product_1)
    category.add_product(product_2)

    products = category._Category__products
    assert len(products) == 1
    assert products[0].quantity == 7
    assert products[0].price == 130000.0


def products_category(category_phone):
    """Тест для проверки геттера products в классе Category."""

    assert category_phone.products == """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт./n
                                        Iphone 15, 210000.0 руб. Остаток: 8 шт./n
                                        Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."""


