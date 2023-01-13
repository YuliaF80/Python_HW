"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

with open('text_5.txt', 'w+', encoding='utf-8') as my_f:
   my_f.write(" ".join([str(randint(1, 100)) for _ in range(20)]))
   my_f.seek(0)
   print(f'Сумма чисел в файле равна: {sum(map(int, my_f.readline().split()))}')


