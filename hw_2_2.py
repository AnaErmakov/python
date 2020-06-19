my_list = input("Введите элементы списка через запятую: ").split(',')

if len(my_list) > 1:
    i = 1
    while i < len(my_list):
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
        i += 2

print(f'Преобразованный список:{my_list}')
