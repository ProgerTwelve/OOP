class Product:
    """Класс для обработки информации о продуктах."""

    name: str  # Название продукта
    description: str  # Описание характеристик продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Магический метод для вывода в консоль информации о продукте (для пользователей)."""

        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод для сложения продуктов.
        Логика сложения должна работать так, чтобы в итоге у вас получалась полная стоимость всех товаров на складе.
        """

        summa = (self.__price * self.quantity) + (
            other.__price * other.quantity
        )

        return summa

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
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
