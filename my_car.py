"""调用car.py文件中的Car类运行程序"""
from car import Car
my_car = Car('audi','a8',2018)
informations =my_car.get_descriptive_name()
print("My new car's information: "+ informations.title())
my_car.odometer_reading = 23
my_car.read_odometer()
