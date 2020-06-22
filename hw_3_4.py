def my_func(var_x=1, var_y=-1):
    """Функция возведения числа в отрицательную степень с применением  **"""

    return 1 / (var_x**abs(var_y))


def my_func_for(var_x=1, var_y=-1):
    """Функция возведения числа в отрицательную степень с применением цикла"""
    res = 1
    for _ in range(abs(var_y)):
        res /= var_x

    return res


x = int(input('Введите число х: '))
y = int(input('Введите степень -у: '))

print(f'Результат ввозведения х**y равен {my_func(x,y)}')
print(f'Результат ввозведения х в степень y через цикл равен {my_func_for(x,y)}')
