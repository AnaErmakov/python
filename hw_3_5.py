def func_sum(num_list=[]):
    """Вычисляет сумму переданного списка элементов"""
    num_int_list = map(int, num_list)
    num_sum = sum(num_int_list)
    return num_sum


number_sum = 0
quit_var = False
# Пока переменная выхода не станет True вычисляем сумму заданных цисел, заданных строкой с пробелами
while not quit_var:
    number_list = input("Введите складываемые числа через пробел или q для выхода: ")
    el = 'q'

    number_list = number_list.split()
    if number_list.count(el) > 0:
        number_list.remove(el)
        quit_var = True

    number_sum += func_sum(number_list)
    print(f'Сумма указанных чисел равна: {number_sum}')
