"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""
import ntpath


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        return '\n'.join('\t'.join([f'{item}' for item in line]) for line in self.matrix) + '\n'
    def __add__(self, other):
        try:
            res = [[self.matrix[line][item] + other.matrix[line][item] for item in range(len(self.matrix[line]))]
                   for line in range(len(self.matrix))]
            return Matrix(res)
        except IndexError:
            return f'Матрицы не соизмеримы'

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[1, 2, 3], [4, 5, 6]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_3)

