import time


class TrafficLight:
    """Класс переключения светофора по заданным временным задержкам"""
    __colour_dict = {'красный': 7, 'желтый': 2, 'зеленый': 5}
    __colour = 'красный'

    def running(self):
        """Функция запуска светофора"""

        for self.__colour, delay in self.__colour_dict.items():
            print(self.__colour)
            time.sleep(int(delay))


# создаем экземпляр класса TrafficLight
t_light = TrafficLight()
# print(t_light._TrafficLight__colour)
t_light.running()
