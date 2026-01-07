class MixinRepr:
    """Класс-миксин для вывода информации об объекте."""

    def __init__(self):
        """Инициализация объекта класса MixinRepr."""

        print(repr(self))

    def __repr__(self):
        """Магический метод __repr__ для класса MixinRepr."""

        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
