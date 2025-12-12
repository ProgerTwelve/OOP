from src.utils import read_json, create_objects_from_json
from unittest.mock import MagicMock, mock_open, patch


def test_read_json_with_mock():
    """Тестирование функции read_json с использованием
    инструмента mock_open и patch"""

    fake_json = '[{"name": "Iphone 15","price": 210000.0}]'

    # Мокаем open так, как будто он читает JSON
    m = mock_open(read_data=fake_json)

    with (
        patch("builtins.open", m),
        patch("os.path.abspath", return_value="fake/path.json"),
        patch(
            "json.load",
            return_value=[{"name": "Iphone 15", "price": 210000.0}],
        ),
    ):
        result = read_json("fake/path.json")

    assert result == [{"name": "Iphone 15", "price": 210000.0}]
    assert isinstance(result, list)
    assert isinstance(result[0], dict)

    m.assert_called_once_with("fake/path.json", "r", encoding="UTF-8")


def test_create_objects_from_json():
    """Тестирование функции create_objects_from_json"""

    json_data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
            ],
        }
    ]

    with (
        patch("src.utils.Product") as MockProduct,
        patch("src.utils.Category") as MockCategory,
    ):

        MockProduct_instance = MagicMock()
        MockCategory_instance = MagicMock()

        # Чтобы любой вызов Product возвращал один и тот же объект
        MockProduct.return_value = MockProduct_instance
        MockCategory.return_value = MockCategory_instance

        result = create_objects_from_json(json_data)

    # Проверяем количество вызовов
    assert MockProduct.call_count == 2  # два продукта
    assert MockCategory.call_count == 1  # одна категория

    # Проверяем вызовы Product
    calls = MockProduct.call_args_list

    # 1 продукт
    args, kwargs = calls[0]
    assert kwargs["name"] == "Samsung Galaxy C23 Ultra"
    assert kwargs["description"] == "256GB, Серый цвет, 200MP камера"
    assert kwargs["price"] == 180000.0
    assert kwargs["quantity"] == 5

    # 2 продукт
    args, kwargs = calls[1]
    assert kwargs["name"] == "Iphone 15"
    assert "Gray space" in kwargs["description"]
    assert kwargs["price"] == 210000.0
    assert kwargs["quantity"] == 8

    # Проверяем вызовы Category
    cat_args, cat_kwargs = MockCategory.call_args
    assert cat_kwargs["name"] == "Смартфоны"
    assert "получение дополнительных функций" in cat_kwargs["description"]
    assert cat_kwargs["products"] == [
        MockProduct_instance,
        MockProduct_instance,
    ]
    assert result == [MockCategory_instance]
