"""创建一个只有子类Electic_car()"""
from car import Car
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has "+str(self.battery_size)+"-kwh battery .")
    """打印一条关于续航历程的信息"""
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 270
        message = "This car can go approximately " + str(range)
        print(message)
    def upgrade_battery(self):
        """9.3.4练习"""
        if self.battery_size != 80:
            self.battery_size = 80
"""子类"""
class ElecticCar(Car):
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery = Battery()
    def describe_battery(self):
        print("This car has a " + str(self.battery) + "_size battery!")
    def describe_information(self):
        informations = self.make.title() +' '+ str(self.year) +' '+ self.model.title()
        print(informations)