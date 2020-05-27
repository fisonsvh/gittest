# Создаем класс Car

class Car:
    car_count = 0

    def start(self, make, name, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        print(make, name, model, sep='\n')
        Car.car_count += 1
        print(Car.car_count)

    def stop(self):
        print("Отключаем двигатель")
