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


def test_add_category(category_with_empty_products, check_add_category):
    """Тест для проверки метода add_product в классе Category."""

    category_with_empty_products.add_product(check_add_category)
    assert len(category_with_empty_products._Category__products) == 1
    assert category_with_empty_products.product_count == 5

