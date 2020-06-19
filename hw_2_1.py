r_list = list('example')  # начальный список

# издеваемся над списком
r_list.append(1)
ex_list = [2.11, 1, 3.14, 'z']
r_list.extend(ex_list)
r_list.pop(-3)
r_list.pop()
r_list.remove(3.14)
r_list.insert(0, 3.14)
r_list.reverse()

# выводим полученный список и типы его элементов
print(f'Следующие типы присутствуют в списке {r_list}:')
for i in r_list:
    print(f'{i}: {type(i)}')


