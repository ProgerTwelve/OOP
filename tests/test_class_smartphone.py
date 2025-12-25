def test_init_smartphone(object_smartphone):
    """Тест для проверки инициализации объекта класса Smartphone."""

    assert object_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert object_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert object_smartphone.price == 180000.0
    assert object_smartphone.quantity == 5
    assert object_smartphone.efficiency == 95.5
    assert object_smartphone.model == "S23 Ultra"
    assert object_smartphone.memory == 256
    assert object_smartphone.color == "Серый"
