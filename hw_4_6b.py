import time
from itertools import cycle

# Создаем исходный список, который будем повторять при помощи cycle()
smiles = ['\U0001f600', '\U0001f623', '\U0001f634', '\U0001f644', '\U0001f602']
t = time.time()

print(f'Повторяющиеся 5 элементов из заданного списка, которые успевает создать cycle() за 0.0003 секунды: ')
for el in cycle(smiles):
    if time.time() - t > 0.0003:
        break
    print(el, end=' ')

print("")
