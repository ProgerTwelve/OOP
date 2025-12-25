from src.class_product import Product


class LawnGrass(Product):
    """Класс для работы с категорией товара трава газонная(Lawn grass).
    Является подклассом класса Product."""

    name: str  # Название продукта
    description: str  # Описание характеристик продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта в наличии
    country: str   # страна-производитель
    germination_period: str  # срок прорастания
    color: str   # цвет

    def __init__(self, name, description, price, quantity, country, germination_period, color ):
        """Конструктор для класса LawnGrass."""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
