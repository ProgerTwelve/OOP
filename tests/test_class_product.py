from src.class_product import Product


def test_init_product(product_iphone):
    """Тестирование инициализации класса Product."""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512 GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_new_product():
    """Тест для проверки метода new_product из класса Product."""

    product_dict = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      }

    new_product = Product.new_product(product_dict)
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.price == 210000.0
    assert new_product.quantity == 8