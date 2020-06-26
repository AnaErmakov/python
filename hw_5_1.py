var_exit = False
print('Для выхода нажмите клавишу Enter')

with open('hw_5_1_text.txt', 'a+') as f:
    while not var_exit:
        new_str = input('Введите значение для добавления в файл: ')
        if new_str != '':
            f.write(new_str + '\n')
        else:
            var_exit = True
