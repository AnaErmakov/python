while True:
    my_str = input("Введите строку: ")

    if len(my_str) > 0:
        my_str = my_str.split()
        i = 0
        for _ in range(len(my_str)):
            print(f'{i + 1} {my_str[i][:10:]}')
            i += 1
        break
    else:
        print("Вы не ввели строку. Попробуйте еще раз\n")
