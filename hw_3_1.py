def division_func(a, b):
    """Производит деление числа а на число b"""
    return a / b


number_a = int(input('Введите делимое:'))
while True:
    number_b = int(input('Введите делитель:'))
    if number_b == 0:
        print('Деление на 0 невозможно')
    else:
        break

res = division_func(number_a,number_b)
print(f'\n{number_a}/{number_b} = {res}')
