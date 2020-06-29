def num_sum(str_var):
    """Функция, возращающая сумму чисел, стоящих перед '(', в передеваемой строке"""
    var_sum = 0
    list_var = str_var.split()
    for el in list_var:
        el = el[0: el.find('(')]
        if el != '':
            var_sum += int(el)
    return var_sum


lines =[]
# Считываем все строки из файла
with open('hw_5_6_text.txt', 'r') as fout:
    lines = fout.readlines()

# Формируем словарь {Предмет: количество часов}
sbj_dict = {}
for line in lines:
    line = line.split(':')
    sbj_dict.update({line[0]: num_sum(line[1])})

print(f'Предмет и общее количество занятий:\n{sbj_dict}')
