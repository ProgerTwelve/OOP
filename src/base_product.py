from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс BaseProduct для класса Product."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Абстрактный метод, который должен быть реализован во всех дочерних классах."""

        pass
