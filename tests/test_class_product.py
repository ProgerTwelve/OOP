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
        "quantity": 8,
    }

    new_product = Product.new_product(product_dict)
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.price == 210000.0
    assert new_product.quantity == 8


def test_getter_price():
    """Проверка геттера на доступ к приватному значению __price класса Product."""

    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product.price == 210000.0


def test_setter_price_cannot_be_zero(product_iphone, capsys):
    """Тест сеттера price для случая price <= 0 класса Product."""

    product_iphone.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_iphone.price == 210000.0


def test_setter_price(product_iphone):
    """Тест сеттера price для случая price > нынешней класса Product."""

    product_iphone.price = 300000.0
    assert product_iphone.price == 300000.0


def test_setter_price_decrease(product_iphone, monkeypatch):
    """Тест сеттера price для случая установления price < нынешней класса Product."""

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product_iphone.price = 90000.0
    assert product_iphone.price == 90000.0


def test_setter_price_rejected(product_iphone, monkeypatch):
    """Тест сеттера price для случая не установления price < нынешней класса Product."""

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product_iphone.price = 90000.0
    assert product_iphone.price == 210000.0


def test_str_product(product_iphone):
    """Тест для проверки магического метода __str__ в классе Product."""

    assert str(product_iphone) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


