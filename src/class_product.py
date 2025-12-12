class Product:
    """Класс для обработки информации о продуктах."""

    name: str  # Название продукта
    description: str  # Описание характеристик продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
