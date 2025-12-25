from src.class_product import Product


class Smartphone(Product):
    """Класс для работы с категорией товаров Смартфоны.
    Является подклассом класса Product."""

    name: str  # Название продукта
    description: str  # Описание характеристик продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта в наличии
    efficiency: float    # производительность
    model: str     # модель
    memory: int    # объем встроенной памяти
    color: str     # цвет

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Конструктор для класса Smartphone."""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
