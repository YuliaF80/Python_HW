"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""
from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def cost_coat(self):
        pass
    @abstractmethod
    def cost_suit(self):
        pass
    def all_costs(self):
        pass
class Clothes(AbstractClass):
    def __init__(self, coat_v, suit_h):
        self.coat_v = coat_v
        self.suit_h = suit_h
        self.cost_coat_v = self.coat_v / 6.5 + 0.5
        self.cost_suit_h = self.suit_h * 2 + 0.3
    @property
    def cost_coat(self):
        return f'Расход ткани на пальто - {round(self.cost_coat_v, 2)}'
    @property
    def cost_suit(self):
        return f'Расход ткани на костюм - {round(self.cost_suit_h, 2)}'
    @property
    def all_costs(self):
        return f'Общий расход ткани - {round(self.cost_suit_h + self.cost_coat_v, 2)}'

costs = Clothes(42, 160)
print(costs.cost_coat)
print(costs.cost_suit)
print(costs.all_costs)


