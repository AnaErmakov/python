# Исходный список чисел
start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Формируем новый список чисел без повторных чисел исходного списка
new_list = [el for el in start_list if start_list.count(el) == 1]

print(f'Исходный список чисел: {start_list}')
print(f'Полученный список чисел: {new_list}')
