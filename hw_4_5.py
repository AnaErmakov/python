from functools import reduce


def multiply_func(prev_el, el):
    """Функция вычисления произведения двух чисел"""
    return prev_el * el


# Формируем список всех четных чисел в пределах от 100 до 1000 включительно
even_numbers = [el for el in range(100, 1001) if el % 2 == 0]

print(f'Результат вычисления произведения всех четных чисел от 100 до 1000 включительно:'
      f'\n{reduce(multiply_func, even_numbers)}')
