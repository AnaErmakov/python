import math
import sys


def fact(n):
    """Функция, для генерации значения факториала от 1 до n"""
    for i in range(1, n+1):
        yield math.factorial(i)


print('Полученный список значений факториала от 1! до n!: ')
for el in fact(int(sys.argv[1])):
    print(el, end=', ')
print('')
