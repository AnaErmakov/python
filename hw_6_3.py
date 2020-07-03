class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())


worker_info = Position('Ivan', 'Ivanov', 'Engineer', 123456, 23456)
print(f'Аттрибуты экземпляра класса Position: \nname: {worker_info.name}, surname: {worker_info.surname}, '
      f'position: {worker_info.position}, {worker_info._income.copy()}\n')
print(f'Полное имя: {worker_info.get_full_name()}')
print(f'Доход с учетом премии: {worker_info.get_total_income()}')
