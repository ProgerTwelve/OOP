from src.class_product import Product


class Category:
    """Класс для обработки информации о категориях продуктовю"""

    name: str  # Название категории
    description: str  # Описание категории
    products: list  # Количество товаров в категории (из класса Product)
    category_count = 0  # Подсчет количества категорий (Атрибут класса)
    product_count = 0  # Подсчет количества продуктов (Атрибут класса)

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    def add_product(self, product: Product):
        """Метод для добавления продуктов в виде объекта класса Product
        в приватный атрибут self.__products класса Category."""

        self.__products.append(product)
        Category.product_count += 1


