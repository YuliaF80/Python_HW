"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def person_func(firstname, lastname, year_born, town, email, num_phone):
    print(f"{firstname} {lastname} {year_born} года рождения, проживает в городе {town}, "
          f"email: {email}, телефон: {num_phone}")
# вызов функции (1 вариант)
person_func(firstname='Юлия', lastname='Федотова', year_born='1980', town='Кострома', email='email@mail.ru', num_phone='+79110000000')
# введение данных (2 вариант)
firstname, lastname, year_born, town, email, num_phone = input('Имя: '), input('Фамилия: '), \
    input('Год рождения: '), input('Город проживания: '), input('Email: '), input('Номер телефона: ')

person_func(firstname, lastname, year_born, town, email, num_phone)
