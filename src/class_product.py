from src.base_product import BaseProduct
from src.mixin_repr import MixinRepr


class Product(BaseProduct, MixinRepr):
    """Класс для обработки информации о продуктах."""

    name: str  # Название продукта
    description: str  # Описание характеристик продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта в наличии

    def __init__(self, name, description, price, quantity):
        """Конструктор класса Product."""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """Магический метод для вывода в консоль информации о продукте (для пользователей)."""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод для сложения продуктов.
        Логика сложения должна работать так, чтобы в итоге у вас получалась полная стоимость всех товаров на складе.
        """
        if type(other) is self.__class__:
            summa = (self.__price * self.quantity) + (
                other.__price * other.quantity
            )

            return summa
        else:
            raise TypeError

    @property
    def price(self):
        """Геттер для получения цены продукта."""

        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для изменения цены продукта."""

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif new_price < self.__price:
            result = input(
                "Вы хотите (y) понизить цену, или хотите оставить цену прежней(n):"
            )
            if result.lower() == "y":
                self.__price = new_price
            else:
                return
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product: dict):
        """Класс-метод, который принимает информацию о продукте в виде словаря
        и возвращает объект класса Product."""

        return cls(**product)
