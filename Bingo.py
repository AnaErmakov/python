import random


class ChoiceError(Exception):
    """Ошибка: Неверный выбор пользователя"""
    def __init__(self, txt):
        self.txt = txt


class Card:
    """Класс карточки лото"""

    def __init__(self):
        self.numbers = Card.add_whitespaces(Card._unique_rand_list(27, 1, 90))

    @staticmethod
    def _unique_rand_list(length, num_start, num_end):
        """Метод возвращает список из length уникальных случайных чисел в заданном диапозоне [num_start: num_end]"""
        numbers = set()
        while len(numbers) < length:
            numbers.add(random.randrange(num_start, num_end))
        return list(numbers)

    @staticmethod
    def add_whitespaces(num):
        """Возвращает список из 27 клеток карточки с заполненными 4 пробелами в каждой из трех строк карточки"""
        for j in range(0, 3):
            for i in Card._unique_rand_list(4, 0, 8):
                num[j * 9 + i] = '  '
        return num

    def cross_out(self, number):
        """Метод, вычеркивающий выпавшие числа"""
        if self.numbers.count(number) > 0:
            self.numbers[self.numbers.index(number)] = '--'
            return True
        return False

    def __str__(self):
        """Вывод на экран в виде карточки 9х3"""
        line = ''
        for i in range(0, 27, 9):
            line += ' '.join(map(lambda el: str(el).rjust(2), self.numbers[i:i + 9])) + '\n'
        line += '-' * 26
        return line


class Game:

    @staticmethod
    def rand_balls():
        """Формируем ряд выпавших номеров бочонков/шаров"""
        nums = [el for el in range(1, 91)]
        random.shuffle(nums)
        return nums

    @staticmethod
    def user_turn(us_card, number):
        while True:
            print(f'Выпало число {number}. Вычеркнуть? (y/n)')
            us_key = input()
            if us_key == 'y':
                if not us_card.cross_out(number):
                    raise ChoiceError('Вы ошиблись, числа ' + str(number) + ' нет в Вашей карточке! Вы проиграли!')
                break
            elif us_key == 'n':
                if us_card.numbers.count(number) > 0:
                    raise ChoiceError('Вы ошиблись, число ' + str(number) + ' было в Вашей карточке! Вы проиграли!')
                break
            elif us_key == 'q':
                print('Game over!')
                exit()
            else:
                print('Вы ввели неккоректное значение')

    @staticmethod
    def start_game():
        print('Для выхода нажмите q \n')
        # Создаем экземляр карточки компьютера
        card_comp = Card()
        print(f'Карточка компьютера:\n{card_comp}')
        # Создаем экземляр карточки игрока
        card_user = Card()
        print(f'Карточка игрока:\n{card_user}')

        # Формируем ряд случайно выпавших шаров
        n = Game.rand_balls()

        try:
            while card_comp.numbers.count('--') < 15 and card_user.numbers.count('--') < 15:
                print(f'(Осталось {len(n) - 1} ходов)')
                card_comp.cross_out(n[0])
                Game.user_turn(card_user, n[0])

                n.remove(n[0])

                print(f'Карточка компьютера:\n{card_comp}')
                print(f'Карточка игрока:\n{card_user}')
            print(f"\n{'Вы выиграли!' if card_user.numbers.count('--' == 15) else 'Выиграл компьютер!'}")
        except ChoiceError as err:
            print(err)


game = Game()
game.start_game()
print("Game over!")
