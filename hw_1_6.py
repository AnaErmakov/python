print('Введите результат первого дня в км')
a = float(input('a = '))
print('Введите желаемый результат в км')
b = float(input('b = '))

i = 1
while b > a:
    i += 1
    a = a * 1.1

print(f'Желаемый результат будет достигнут на {i} день')
