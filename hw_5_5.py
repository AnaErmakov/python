# Создаем строку чисел, разделенных пробелами, для записи в файл
numbers_str = '911 2 3 4 5 6 7 8 9 10 11 12 13 14 15'

# Записываем строку в файл
with open('hw_5_5_text.txt', 'w') as f:
    print(numbers_str, file=f)

numbers = []
# Считываем числа, записанные в файле
with open('hw_5_5_text.txt', 'r') as fout:
    for line in fout:
        numbers += list(map(int, line.split()))

print(f'Числа, записанные в файле: {numbers}')
print(f'Сумма чисел равна: {sum(numbers)}')
