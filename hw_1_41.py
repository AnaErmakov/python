print("Введите целое положительное число")
n = int(input("n = "))

i = n
max_n = 0
while i > 0:
    if max_n <= i%10:
        max_n = i%10
    i = i//10

print(f'Наибольшая цифра в числе {n}: {max_n}')