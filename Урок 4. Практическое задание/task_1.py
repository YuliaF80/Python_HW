"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, name_emp, work_hours, rate_per_hour, reward = argv
"""
print('Имя скрипта: ', script_name)
print('ФИО сотрудника: ', name_emp)
print('Отработано в часах: ', work_hours)
print('Ставка в час: ', rate_per_hour)
print('Премия: ', reward)
"""

def my_func(work_hours, rate_per_hour, reward): # функция вычисления заработной платы
    try:
        print(f'Заработная плата сотрудника {name_emp}: {(float(work_hours) * float(rate_per_hour)) + float(reward)}')
    except ValueError:
        print('Неверно ввели данные')

my_func(work_hours, rate_per_hour, reward)

