import sys


def payroll(hours_a_month, rate, motivation):
    """Функция для расчета суммы зарплаты сотрудника в месяц с внешними аргументами"""
    # salary = hours_a_month * rate + motivation

    return print(f'Заработная плата сотрудника в месяц: {hours_a_month * rate + motivation}')


payroll(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
