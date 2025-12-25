def test_init_lawngrass(object_lawngrass):
    """Тест для проверки инициализации объекта класса LawnGrass."""

    assert object_lawngrass.name == "Газонная трава"
    assert object_lawngrass.description == "Элитная трава для газона"
    assert object_lawngrass.price == 500.0
    assert object_lawngrass.quantity == 20
    assert object_lawngrass.country == "Россия"
    assert object_lawngrass.germination_period == "7 дней"
    assert object_lawngrass.color == "Зеленый"
