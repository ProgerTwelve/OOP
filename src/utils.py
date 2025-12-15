import json
import os

from src.class_category import Category
from src.class_product import Product


def read_json(path: str) -> list[dict]:
    """Функция для преобразования json-файла в словарь."""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list[dict]) -> list[object]:
    """Преобразует данные, полученные из json-файла
    в список объектов класса Category."""

    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
