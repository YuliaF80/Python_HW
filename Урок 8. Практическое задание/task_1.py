"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class DataClass:
    day_month_year = '30-01-2023'
    @classmethod
    def my_data(cls):
        """1 вариант
        cls.day = int(cls.day_month_year.split(".")[0])
        cls.month = int(cls.day_month_year.split(".")[1])
        cls.year = int(cls.day_month_year.split(".")[2])"""
        #более компактный вариант
        cls.day, cls.month, cls.year = [int(el) for el in cls.day_month_year.split("-")]
        return f"Число - {cls.day}, месяц - {cls.month}, год - {cls.year}"
    @staticmethod
    def check_my_data():
        if DataClass.day >= 0 or DataClass.day <= 31:
            if DataClass.month >= 0 or DataClass.month <= 12:
                if DataClass.year >= 0:
                    return f'Формат даты верный'
                else:
                    return f'Неверный формат даты'
            else:
                return f'Неверный формат даты'
        else:
            return f'Неверный формат даты'

print(DataClass.my_data())
print(DataClass.check_my_data())


