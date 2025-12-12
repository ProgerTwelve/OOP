def test_init_product(product_iphone):
    """Тестирование инициализации класса Product."""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512 GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8
