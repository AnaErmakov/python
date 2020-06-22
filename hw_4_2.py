# Исходный список
start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Формируем новый список
new_list = [el for el in start_list[1:] if el > start_list[start_list.index(el) - 1]]

print(f'Исходный список: {start_list}')
print(f'Сформированный список: {new_list}')
