"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} поехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn(self, direction):
        return f'{self.name} повернула {direction}'
    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed} км/ч'
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f'Текущая скорость автомобиля {self.name} превышает разрешенную скорость на {self.speed - 60}'
        else:
            return f'Текущая скорость автомобиля {self.name} в пределах разрешенной'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed} км/ч'
    def police(self):
        return (f'Автомобиль {self.name} является полицейской: {self.is_police}')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость автомобиля {self.name} превышает разрешенную скорость на {self.speed - 40} км/ч'
        else:
            return f'Текущая скорость автомобиля {self.name} в пределах разрешенной'
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'

Volkswagen_Golf = TownCar(55, "Красный", "Фольксваген Гольф", False)
Porsche_918_Spyder = SportCar(150, "Черный", "Порше 918", False)
Mitsubishi_L200 = WorkCar(50, "Коричневый", "Митсубиси Л200", False)
Ford = PoliceCar(90, "Черный", "Форд", True)

print(f'Цвет автомобиля {Volkswagen_Golf.name} - {Volkswagen_Golf.color}')
print(f'Цвет автомобиля {Porsche_918_Spyder.name} - {Porsche_918_Spyder.color}')
print(f'Цвет автомобиля {Mitsubishi_L200.name} - {Mitsubishi_L200.color}')
print(f'Цвет автомобиля {Ford.name} - {Ford.color}')
print(f'Автомобиль {Mitsubishi_L200.name} принадлежит полиции? {Mitsubishi_L200.is_police}')
print(Mitsubishi_L200.show_speed())
print(Porsche_918_Spyder.show_speed())
print(Ford.police())
print(Volkswagen_Golf.show_speed())



