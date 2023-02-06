"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class OwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt

# склад оборудования
class WareHouse_Equipment:
    equipments = []  # список оборудования на складе

    @classmethod
    def add_to(cls, equipment):  # добавление оборудования на склад, исключая добавление пустых словарей
        if equipment.eq_list != {}:
            cls.equipments.append(equipment.eq_list)
        else:
            print('Параметры отсутствуют')

    @classmethod
    def extract(cls, equipment, count=1):  # передача оборудования в отдел, учитывая остаток оборудованя на складе
        try:
            if equipment.eq_list['Количество'] - count >= 0:
                equipment.eq_list['Количество'] -= count
            else:
                raise OwnExc(f'Необходимое количество оборудования отсутствует, '
                             f'остаток {equipment.eq_list["Количество"]}')
        except OwnExc as err:
            print(err.txt)

# класс оборудования
class Equipment:
    def __init__(self, name, model, quantity, number_pages):
        self.name = name
        self.model = model
        self.number_pages = number_pages
        try:
            if type(quantity) == int:
                self.quantity = quantity
                self.eq_list = {
                    f'Наименование {self.__class__.__name__}': self.name,
                    'Модель': self.model,
                    'Количество': self.quantity
                }
            else:
                self.eq_list = {}
                raise OwnExc('Ошибка ввода: вы ввели не число')
        except OwnExc as er:
            print(er.txt)

# классы наследников: принтеры, сканеры, копиры
class Printer(Equipment):
    def print_par(self):
        return f'{self.name} {self.model} печатает {self.number_pages} страниц в минуту'


class Scanner(Equipment):
    def scan_par(self):
        return f'{self.name} {self.model} сканирует {self.number_pages} страниц в минуту'


class Xerox(Equipment):
    def xerox_par(self):
        return f'{self.name} {self.model} копирует {self.number_pages} страниц в минуту'


# создание склада
stock = WareHouse_Equipment()
# создание объектов: офисное оборудование
printer1 = Printer('Samsung', 'q', 'E100', 6)
printer2 = Printer('Samsung', 'E100', 3, 6)
printer3 = Printer('HP', '2000', 3, 15)
scaner1 = Scanner('HP', '200', 2, 10)
xerox1 = Xerox('Canon', 'C300', 3, 20)
# добавление объектов на склад
stock.add_to(printer1)
stock.add_to(printer2)
stock.add_to(printer3)
stock.add_to(scaner1)
stock.add_to(xerox1)
print()
print(stock.equipments)
print()
# печать параметров оборудования
print(printer2.print_par())
print(scaner1.scan_par())
print(xerox1.xerox_par())
print()
# передача оборудования со склада
stock.extract(printer2)
print(stock.equipments)
print()
stock.extract(printer3, 4)
print(stock.equipments)

