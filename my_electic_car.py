"""引用电动汽车的类运行程序"""
from 9.3.py import ElecticCar
my_new_electic_car = ElecticCar('ama','size-1','2012')
my_new_electic_car.battery.describe_battery()
my_new_electic_car.battery.get_range()
"""引用电动汽车和汽车的类运行程序"""
from car import ElecticCar,Car
my_car_0 = Car('toyota','a5',2011)
print(my_car_0.get_descriptive_name())
my_electic_car_0 = ElecticCar('ali','sd',2000)
my_electic_car_0.describe_information()
"""引用car.py这个模块"""
import car
print("\n")
my_car_1 = car.Car('crv','news','2018')
print(my_car_1.get_descriptive_name())
my_electic_car_1 = ElecticCar('lid','ds',2013)
my_electic_car_1.describe_information()
"""引用模块中的所有类"""
from car import *
print("\n")
my_car_1 = car.Car('crv','news','2018')
print(my_car_1.get_descriptive_name())
my_electic_car_1 = ElecticCar('lid','ds',2013)
my_electic_car_1.describe_information()
"""导入Restaurant类"""
from restaurant import Resaurant
my_favorate_food = Resaurant('早茶店','粤菜')