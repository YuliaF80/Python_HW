"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    try:
        nums = input('Введите число, нажмите Enter (для выхода введите "q"): ')
        if nums == 'q':
            break
        if not nums.isdigit():
            raise OwnError('Ошибка ввода')
        my_list.append(nums)
    except OwnError as err:
        print(err)

print(f'Список чисел - {my_list}')
