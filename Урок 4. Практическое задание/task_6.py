"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

# итератор, генерирующий целые числа, начиная с указанного
lower_limit, upper_limit = int(input('Введите нижний предел целых чисел: ')),\
    int(input('Введите верхний предел целых чисел: '))
for el in count(lower_limit):
    if el > upper_limit:
        break
    else:
        print(el)

# итератор, повторяющий элементы некоторого списка, определенного заранее

my_list = [10, 24, 9.8, 2]
print(f'Список: {my_list}')
my_iter = cycle(my_list)

# 1 вариант (ограничение повторений количеством элементов в списке)
print('1 вариант итерации, повторяющий элементы списка:', my_list)
i = 0
for el in my_iter:
    if i >= len(my_list):
        break
    print(el)
    i += 1

# 2 вариант (с возможностью задать количество повторений элементов списка)
num = int(input('2 вариант - введите количество повторений элементов списка: '))
c = 0
while c <= (num - 1):
    print(next(my_iter))
    c += 1

