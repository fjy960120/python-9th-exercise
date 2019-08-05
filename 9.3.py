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
"""创建一个分支类"""
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
        information = self.make.title + str(self.year) + self.model.title()
        print(information)

my_electic_car = ElecticCar('ama','s-42',2016)
print(my_electic_car.get_descriptive_name())
my_electic_car.battery.describe_battery()
my_electic_car.battery.get_range()
my_electic_car.battery.upgrade_battery()
my_electic_car.battery.get_range()



"""9.3.1练习"""

"""父类：9.1练习"""
class Resaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisinetype = cuisine_type
    def describe_restaurant(self):
        print("\nThis restaurant's name is : "+ self.name.title())
        print("The restaurant's cuisine type are : "+self.cuisinetype.title())
    def open_restaurant(self):
        print("This reataurant is openning!")

"""子类：冰淇淋"""
class IceCreamStand(Resaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['coffe','chocolate','mango']
    def describe_icecream(self):
        print("You flavors icecream style are:")
        for i in self.flavors :
            print("\t" + i.title())
my_icecream = IceCreamStand('早茶店','粤菜')
print(my_icecream.describe_icecream())

"""9.3.2练习"""
"""父类：User"""
class User():
    def __init__(self,frist_name,last_name):
        self.fristname = frist_name
        self.lastname = last_name
        self.users = { 'age':16,'location':'beijing'}
    def describe_user(self):
        print("\nUsers information is: ")
        print("\t users frist name is: "+ self.fristname.title())
        print("\t users last name is: "+ self.lastname.title())
        print("\n Users other information are: ")
        for j,k in users.items():
            users[j]=k
            print("\t"+j.title()+" : "+self.j.title())
    def greet_user(self):
        print("\nHello! "+self.fristname.title()+self.lastname.title())
"""子类：管理员"""
class Privileges():
    def __init__(self,privileges):

        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        print("These are admin's privileges: ")
        for i in self.privileges:
            print("\t" + i.title())
class Admin(User):
    def __init__(self,frist_name,last_name):
        super().__init__(frist_name,last_name)
        self.privilege = Privileges({})
frist_admin = Admin('lily','edward')
frist_admin.privilege.show_privileges()
"""9.3.3练习"""
class Family():
    def __init__(self,frist_name,last_name,age):
        self.frists = frist_name
        self.lasts = last_name
        self.ages = age
    def family_informations(self):
        print("您的家庭成员信息是：")
        information = self.frists.title() + self.lasts.title() + str(self.ages)
        print("\n\t" + information + ".")
my_family = Family('lily','edward',20)
my_family.family_informations()
