def my_func(var_a=0, var_b=0, var_c=0):
    """Вычисляет сумму двух максимальных элементов из трех переданных"""
    list_args = [var_a, var_b, var_c]
    two_args_sum = max(list_args)
    list_args.remove(two_args_sum)
    two_args_sum += max((list_args))
    return two_args_sum


a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

print(f'Сумма двух наибольших из заданных чисел равна {my_func(a,b,c)}')
