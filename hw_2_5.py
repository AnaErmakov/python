my_list = [8, 7, 5, 5, 3, 3, 2]
new_r = 0

while True:
    new_r = int(input("Введите новое значение рейтинга: "))

    if new_r >= 0:
        n = my_list[0]
        i = 0
        while my_list[i] >= new_r:
            i += 1
            if i == len(my_list):
                i += 1
                break

        my_list.insert(i,new_r)
        print(f'\nНовое значение рейтинга было вставлено на {i+1} позицию')
        print(f'Полученный список значений рейтинга: {my_list}')
        break

    else: print('Вы ввели неверное значение рейтинга. Попробуйте еще раз\n')
