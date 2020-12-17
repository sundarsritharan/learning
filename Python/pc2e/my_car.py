"""
from car import Car,ElectricCar

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_beetle_car = Car('volkswagen','beetle',2019)
print(my_beetle_car.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2020)
print(my_tesla.get_descriptive_name())

import car 

my_beetle_car = car.Car('volkswagen','beetle',2019)
print(my_beetle_car.get_descriptive_name())

my_tesla = car.ElectricCar('tesla','roadster',2020)
print(my_tesla.get_descriptive_name())


from car import Car
from electric_car import ElectricCar as

my_beetle_car = Car('volkswagen','beetle',2019)
print(my_beetle_car.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2020)
print(my_tesla.get_descriptive_name())

"""
from car import Car
from electric_car import ElectricCar as EC
    
my_beetle_car = Car('volkswagen','beetle',2019)
print(my_beetle_car.get_descriptive_name())

my_tesla = EC('tesla','roadster',2020)
print(my_tesla.get_descriptive_name())