class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')


class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка")

    def draw(self):
        super().draw()
        print(f'Для отрисовки используется {self.title}')


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Карандаш")

    def draw(self):
        super().draw()
        print(f'Для отрисовки используется {self.title}')


class Handle(Stationery):
    def __init__(self):
        super().__init__("Маркер")

    def draw(self):
        super().draw()
        print(f'Для отрисовки используется {self.title}')


# Создаем экземпляр класса Pen
pen = Pen()
pen.draw()

# Создаем экземляр класса Pencil
pencil = Pencil()
pencil.draw()

# Создаем экземпляр класса Handle
handle = Handle()
handle.draw()
