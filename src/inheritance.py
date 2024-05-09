'''Створити клас Vehicle з властивостями make, model, year та weight, та методом start_engine().

Створити підклас Car, який є нащадком Vehicle, з додатковими властивостями num_doors
та num_passengers, та метод drive().
Перевизначити метод start_engine(), щоб виводити "The car's engine is starting...".

Створити підклас Truck, який є нащадком Vehicle, з додатковими властивостями cargo_capacity та
towing_capacity, та метод haul(). Перевизначити метод start_engine(),
щоб виводити "The truck's engine is starting...".

Створити підклас Motorcycle, який є нащадком Vehicle, з
додатковими властивостями num_wheels та has_sidecar, та метод ride().
Перевизначити метод start_engine(), щоб виводити "The motorcycle's engine is starting...".

Створити екземпляр об'єкта з кожного підкласу та викликати їх відповідні методи. Продемонструвати
 використання поліморфізму, викликаючи метод start_engine() на кожному об'єкті.'''
class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
    def start_engine(self):
        print("The vehicle's engine is starting...")
class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers
    def drive(self):
        print("The car")
    def start_engine(self):
        print("The car's engine is starting...")
class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity
    def haul(self):
        print("The truck")
    def start_engine(self):
        print("The truck's engine is starting...")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar
    def ride(self):
        print("The motorcycle")
    def start_engine(self):
        print("The motorcycle's engine is starting...")
'''car1 = Car("Audi", "rs7", 2022, 2020, 4, 5)
truck1 = Truck("Ford", "F-150", 2020, 4000, 2000, 10000)
motorcycle1 = Motorcycle("Kawasaki", "H2 SX SE", 2021, 256, 2, False)
car1.start_engine()
car1.drive()
truck1.start_engine()
truck1.haul()
motorcycle1.start_engine()
motorcycle1.ride()'''

