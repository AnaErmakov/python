f_lines = []
with open('hw_5_3_text.txt', 'r') as f:
    f_lines = f.readlines()

print('Список сотрудников, оклад которых менее 20000:')
sum = 0
empty_lines = 0
for line in f_lines:
    line = line.split()
    if len(line) == 2:
        if int(line[1]) < 20000:
            print(line[0])
        sum += int(line[1])
    else:
        empty_lines += 1

sum /= len(f_lines) - empty_lines
print(f'Средняя величина оклада: {sum}')
