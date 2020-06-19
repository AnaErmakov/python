goods_list = []
key_list = ['Название: ', 'Цена: ', 'Количество: ', 'Ед: ']
name_set = set()
price_set = set()
number_set = set()
measure_set = set()

while True:

    count = int(input('Укажите требуемое количество товаров в структуре: '))
    if count > 0:
        i = 0
        while i < count:
            i += 1
            name = input(key_list[0])
            price = input(key_list[1])
            number = input(key_list[2])
            measure = input(key_list[3])

            ch_dict = {key_list[0]: name, key_list[1]: price, key_list[2]: number,
                       key_list[3]: measure}
            el = (i,ch_dict)
            goods_list.append(el)

            name_set.add(name)
            price_set.add(price)
            number_set.add(number)
            measure_set.add(measure)

        analytics_dict = {key_list[0]: name_set, key_list[1]: price_set, key_list[2]: number_set,
                          key_list[3]: measure_set}

        print('\nПолученная структура Товары:')
        for el in goods_list:
            print(el)
        print('\nПолученный словарь аналитики товаров:')
        for el in analytics_dict.items():
            print(el)
        break
    else:
        print("Вы ввели неверное количество товаров. Попробуйте еще раз")
