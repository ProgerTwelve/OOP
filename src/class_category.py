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

    def __str__(self):
        """Строковое отображение класса Category в следующем виде: Название категории, количество продуктов: 200 шт.
        Здесь количество продуктов считается из общего числа всех продуктов на складе.
        """

        counting_quantity_products = 0
        for prod in self.__products:
            counting_quantity_products += prod.quantity

        return f"{self.name}, количество продуктов: {counting_quantity_products} шт."

    def add_product(self, product: Product):
        """Метод для добавления продуктов в виде объекта класса Product
        в приватный атрибут self.__products класса Category."""

        for (
            prod
        ) in (
            self.__products
        ):  # Цикл для проверки наличия добавляемого продукта в списке продуктов
            if (
                prod.name == product.name
            ):  # Если добавляемый продукт уже есть в списке класса
                prod.quantity += (
                    product.quantity
                )  # Просто плюсуем количество добавляемого продукта в нашем списке
                prod.price = max(
                    prod.price, product.price
                )  # Ставим наибольшую цену
                return  # Выходим из метода

        # Если продукта нет в списке продуктов, то добавляем продукт полностью
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для возвращения информации о продуктах в виде
        "Название продукта, X руб. Остаток: X шт.\n" """

        products_information = ""
        for product in self.__products:
            products_information += str(product) + "\n"

        return products_information
