from abc import ABC, abstractmethod


class Clothers(ABC):
    """Абстрактный класс Clothers"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothers):
    """Класс для расчета материала на пальто"""

    def __init__(self, size):
        super().__init__('coat')
        self.size = size

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5)


class Costume(Clothers):
    """Класс для расчета материала на костюм"""

    def __init__(self, height):
        super().__init__('costume')
        self.height = height

    @property
    def consumption(self):
        return round(2 * self.height + 0.3)


coat = Coat(48)
print(f'Требуется {coat.consumption}м материала на пальто {coat.size} размера')

costume = Costume(1.7)
print(f'Требуется {costume.consumption}м материала на костюм для {costume.height}м роста')
