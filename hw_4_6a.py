import sys
from itertools import count

num = int(sys.argv[1])
print(f'Список из 20 целых чисел, начиная с {num}: ')

for el in count(num, 1):
    if el >= num + 20:
        break
    else: print(el, end=' ')
print('')
