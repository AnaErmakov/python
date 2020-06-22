def user_data_print(name='', sec_name='', b_year='', city='', email='', phone=''):
    """Выводит на экран введенные данные о пользователе.

    Именованные параметры:
    name -- имя пользователя
    sec_name -- фамилия пользователя
    b_year -- год рождения пользователя
    city -- город проживания
    email -- адрес электронной почты пользователя
    phone -- телефон пользователя

    """
    
    print(f'\nДанные пользователя: {name}, {sec_name}, {b_year}, {city}, {email}, {phone}.')


print('Пожалуйста, далее введите данные пользователя')
name = input('Введите имя пользователя: ')
sec_name = input('Введите фамилию пользователя: ')
b_year = input('Введите год рождения пользователя: ')
city = input('Введите город проживания пользователя: ')
email = input('Введите email пользователя: ')
phone = input('Введите телефон пользователя: ')

user_data_print(name=name, sec_name=sec_name, city=city, phone=phone, b_year=b_year, email=email)
