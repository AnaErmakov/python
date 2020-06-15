print('Введите время в секундах:')
sec = int(input())

print(f'\n{sec} секунд равно {sec//3600}ч {sec%3600//60}мин {sec%60}сек')
