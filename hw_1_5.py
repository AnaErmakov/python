print('Введите сумму выручки')
proceeds = float(input())

print('Введите сумму издержек')
expenses = float(input())

if proceeds >= expenses:
    revenue = proceeds - expenses
    profitableness = revenue/proceeds
    print(f'Прибыль компании составила: {revenue} \nРентабельность: {profitableness}')
    print('Введите количество сотрудников компании:')
    number = int(input())
    print(f'Прибыль компании в рассчете на одного сотрудника равна {revenue/number}')
else:
    loss = expenses - proceeds
    print('Убыток компании составил: {loss}')
