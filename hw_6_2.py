class Road:

    def __init__(self, length, width):
        """Определяем класс Road с атрибутами длины length и ширины width дороги"""
        self._length = length
        self._width = width

    def road_weight(self, weight, thickness):
        """Функция расчета массы асфальта с заданной массой weight кг/м2 и толщиной thickness см"""
        return self._length * self._width * weight * thickness


# Создаем экземпляр класса Road
road = Road(20, 5000)
print(road.road_weight(25, 5))
