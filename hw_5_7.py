import json

firms = {}
s_profit = 0
count_profit = 0

# Считываем из файла данные по фирмам и рассчитываем суммарную прибыль по всем безубыточным фирмам
with open('hw_5_7_text.txt', 'r') as f:
    for line in f:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        firms.update({line[0]: profit})
        if profit > 0:
            s_profit += profit
            count_profit += 1

# Получаем среднюю прибыль по безубыточным фирмам
s_profit /= count_profit

# Создаем окончательный список фирм с их прибылью и средней прибылью по безубыточным фирмам
res_list = [firms, {'average_profit': int(s_profit)}]

# Записываем результат фомате json
with open('hw_5_7_data.json', 'w') as fin:
    json.dump(res_list, fin)
