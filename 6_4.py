class Car:
    def __init__(self, name, color, speed, is_police= False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"{self.name} Поехали!")

    def stop(self):
        print(f"{self.name} Остановка")

    def turn(self, direction):
        print(f" {self.name} Поворот {'налево' if direction == 0 else 'направо'}")

    def show_speed(self):
        print (f"{self.name} Скорость автомобиля {self.speed}")

class TownCar(Car):

    def show_speed(self):
        return print(f"{self.name} Превышение скорости!" if self.speed > 60 else f" Скорость автомобиля - {self.speed}")

class SportCar(Car):
    """Спортивный автомобиль"""

class WorkCar(Car):

    def show_speed(self):
        return print(f"{self.name} Превышение скорости!" if self.speed > 40 else f" Скорость автомобиля - {self.speed}")

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police = True):
        Car.__init__(self, name,color,speed,is_police)

my_car = TownCar("Енот", "Красный", 70)
my_car.go()
my_car.show_speed()
police_car = PoliceCar("Полиция", "Синий", 90)
police_car.turn(1)