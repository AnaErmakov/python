index = 000
name_str = ''
cost = '0.00'

i = 0
while i < 3:
    i += 1
    print('Введите артикул:')
    index = input()
    print('Введите наименование товара')
    name_str = input()
    print('Введите Стоимость:')
    cost = input()

    if i == 1:
        line1 = f'Артикул: {index}  Наименование: {name_str}  Цена: {cost}'
    elif i == 2:
        line2 = f'\nАртикул: {index}  Наименование: {name_str}  Цена: {cost}'
    else:
        line3 = f'\nАртикул: {index}  Наименование: {name_str}  Цена: {cost}'

print(line1,line2,line3)