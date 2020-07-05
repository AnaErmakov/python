class Cell:
    """Класс для описания Клетки, содержащей несколько ячеек"""

    def __init__(self, slots):
        self.slots = slots

    def __add__(self, other):
        return Cell(self.slots + other.slots)

    def __sub__(self, other):
        return Cell(self.slots - other.slots) if self.slots - other.slots > 0 else 'Разность количества ' \
                                                                                   'ячеек двух клеток меньше 0!'

    def __mul__(self, other):
        return Cell(self.slots * other.slots)

    def __floordiv__(self, other):
        return Cell(self.slots // other.slots)

    def make_order(self, length):
        """Метод, визуально преобразующий количество ячеек Клетки в матрицу"""
        return ('*' * length + '\n') * (self.slots // length) + '*' * (self.slots % length)

    def __str__(self):
        return '*' * self.slots


cell1 = Cell(34)
cell2 = Cell(24)

print(f'Клетка1 + Клетка2:\n{(cell1 + cell2).make_order(17)}')
print(f'Клетка1 - Клетка2:\n{cell1 - cell2}')
print(f'Клетка2 - Клетка1:\n{cell2 - cell1}')
print(f'Клетка1 * Клетка2:\n{(cell1 * cell2).make_order(57)}')
print(f'Клетка1 // Клетка2:\n{cell1 // cell2}')
