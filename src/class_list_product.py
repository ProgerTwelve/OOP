from src.class_category import Category


class ListProduct:
    """Класс для получения возможности итерации по продуктам из класса Category."""

    category: Category  # атрибут category является экземпляром класса Category

    def __init__(self, category):
        """Инициализация класса ListProduct."""

        self.category = category
        self.index = 0

    def __iter__(self):
        """Магический метод __iter__ для получения итератора для перебора объекта ."""

        return self

    def __next__(self):
        """Магический метод __next__ для перехода к следующему значению."""

        list_products = self.category.products.split("\n")

        if self.index < len(list_products):
            result = list_products[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
