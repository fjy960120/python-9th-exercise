class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        information = self.make + ' ' + self.model + ' '+  str(self.year)
        return information.title()
    def read_odometer(self):
        print("\nThis car has :"+str(self.odometer_reading)+" miles on it!")
    def updata_odometer(self,milian):
        self.odometer_reading = milian
    def updata_odometer_0(self,milian_0):
        if milian_0 >= self.odometer_reading:
            self.odometer_reading = milian_0
        else:
            print("\n\tDon't do this!")
    def updata_odometer_1(self,milian):
        self.odometer_reading += milian
my_car = Car('audi','a8',2018)
my_car.get_descriptive_name()
print(my_car.get_descriptive_name())
my_car.updata_odometer(20)
my_car.read_odometer()
my_car.updata_odometer_0(10)
my_car.read_odometer()
my_car.updata_odometer_1(30)
my_car.read_odometer()

"""9.2.1练习"""
class Restaurant():
    def __init__(self,name,cookstyle):
        self.name = name
        self.cookstyle = cookstyle
        self.number_served = 0
    def serverd_number(self):
        print("\nThis restaurant has serverd "+ str(self.number_served)+".")
    def set_number_serverd(self,number):
        self.number_served = number
    def increment_number_served(self,number):
        self.number_served += number
resaurant_0 = Restaurant('chinese style','chinese')
resaurant_0.serverd_number()
resaurant_0.number_served=20
resaurant_0.serverd_number()
resaurant_0.set_number_serverd(56)
resaurant_0.serverd_number()
resaurant_0.increment_number_served(22)
resaurant_0.serverd_number()
"""9.2.2练习"""
class User():
    def __init__(self,frist_name,last_name,login_attempts):
        self.frist = frist_name
        self.last = last_name
        self.login = login_attempts
    def increment_login_attempts(self):
        self.login += 1
    def reset_login_attempts(self):
        self.login = 0
    def reading_login(self):
        print(self.frist.title()+self.last.title())
        print("The login is : " + str(self.login))
user_0 = User('lily','edward',5)
user_0.reading_login()
user_0.increment_login_attempts()
user_0.reading_login()
user_0.reset_login_attempts()
user_0.reading_login()
