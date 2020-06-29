var_exit = False
print('Для выхода нажмите клавишу Enter')

with open('hw_5_2_text.txt', 'a+') as f:
    while not var_exit:
        new_str = input('Введите значение для добавления в файл: ')
        if new_str != '':
            f.write(new_str + '\n')
        else:
            var_exit = True

    f.seek(0)
    i = 0
    print('Количество слов в строке: ')
    for line in f:
        i += 1
        f_line = line.split()
        print(len(f_line), end=', ')
    print(f'Количество строк в файле: {i}')
