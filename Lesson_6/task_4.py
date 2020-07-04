# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и
# также покажите результат.


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала.")

    def stop(self):
        print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        if direction == "l":
            print(f"Машина {self.name} повернула налево.")
        elif direction == "r":
            print(f"Машина {self.name} повернула направо.")
        else:
            print("Направление не задано!")

    def show_speed(self):
        print(f"Скорость машины {self.name}: {self.speed}.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость машины {self.name}: {self.speed}. Превышение скорости!")
        else:
            print(f"Скорость машины {self.name}: {self.speed}.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость машины {self.name}: {self.speed}. Превышение скорости!")
        else:
            print(f"Скорость машины {self.name}: {self.speed}.")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar('городская', 'черная', 50)
town_car.go()
town_car.stop()
town_car.turn("l")
town_car.show_speed()

work_car = WorkCar('рабочая', 'белая', 50)
work_car.go()
work_car.stop()
work_car.turn("r")
work_car.show_speed()

sport_car = SportCar('спортивная', 'красная', 50)
sport_car.go()
sport_car.stop()
sport_car.turn("l")
sport_car.show_speed()

police_car = PoliceCar('полицейская', 'синяя', 50)
police_car.go()
police_car.stop()
police_car.turn("r")
police_car.show_speed()
