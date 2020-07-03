class Car:
    def __init__(self, colour):
        self.speed = 0
        self.colour = colour
        self.name = ''
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.colour} {self.name} поехала со скоростью {speed}')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью  {self.speed}')


class TownCar(Car):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = 'Town car'

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Внимание! Превышение скорости!')


class WorkCar(Car):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = 'Work car'

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Внимание! Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = 'Police car'
        self.is_police = True


class SportCar(Car):
    def __init__(self, colour):
        super().__init__(colour)
        self.name = 'Sport car'


town_car = TownCar('red')
town_car.go(50)
town_car.turn('направо')
town_car.show_speed()
town_car.go(80)
town_car.show_speed()
town_car.stop()
print(f"Это полицейская машина? {'Да' if town_car.is_police else 'Нет'}\n")

police_car = PoliceCar('blue')
police_car.go(80)
police_car.speed = 50
police_car.show_speed()
print(f"Это полицейская машина? {'Да' if police_car.is_police else 'Нет'}\n")

sport_car = SportCar('black with white stripes')
sport_car.go(80)
sport_car.show_speed()
sport_car.turn('around')
sport_car.stop()
print(f"Это полицейская машина? {'Да' if town_car.is_police else 'Нет'}\n")

work_car = WorkCar('yellow')
work_car.go(30)
work_car.turn('налево')
work_car.show_speed()
work_car.go(50)
work_car.show_speed()
work_car.stop()
