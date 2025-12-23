import pytest


def test_list_product(list_iterator):
    """Тест для проверки класса ListProduct на возможность итерирования."""

    iter(list_iterator)
    assert list_iterator.index == 0
    assert (
        next(list_iterator)
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )
    assert next(list_iterator) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert (
        next(list_iterator)
        == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert next(list_iterator) == ""
    with pytest.raises(StopIteration):
        next(list_iterator)
