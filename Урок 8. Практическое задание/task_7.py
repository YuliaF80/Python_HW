"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

compl1 = Complex(-1, 2)
compl2 = Complex(3, -4)
print(compl1 + compl2)
print(compl1 * compl2)
# проверка
print(complex(-1, 2) + complex(3, -4))
print(complex(-1, 2) * complex(3, -4))