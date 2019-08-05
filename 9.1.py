class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is siting now")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" is rulling over now")
my_dog = Dog('willian',6)
print("My dog's name is : "+my_dog.name.title())
print("My dog's age is : "+ str(my_dog.age))
my_dog.sit()
my_dog.roll_over()
your_dog = Dog('alice',5)
lily_dog = Dog('beta',5)
print("Lily have a dog ,It's name is : "+lily_dog.name.title())
print("Your dog's name is : " + your_dog.name.title())
print("Lily have a dog,It's age is "+str(lily_dog.age))
lily_dog.sit()
lily_dog.roll_over()
"""9.1.1练习"""
class Resaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisinetype = cuisine_type
    def describe_restaurant(self):
        print("\nThis restaurant's name is : "+ self.name.title())
        print("The restaurant's cuisine type are : "+self.cuisinetype.title())
    def open_restaurant(self):
        print("This reataurant is openning!")
restaurant = Resaurant('homoo','chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant_0 = Resaurant('毛肚火锅店','川菜')
restaurant_0.describe_restaurant()
restaurant_1 = Resaurant('炸酱面店','北京菜')
restaurant_1.describe_restaurant()
restaurant_2 = Resaurant('早茶店','粤菜')
restaurant_2.describe_restaurant()
"""9.1.3练习"""
class User():
    def __init__(self,frist_name,last_name,**users):
        self.fristname = frist_name
        self.lastname = last_name
        self.users = users
       # for j,k in users.items():
         #   users[j]=k
            #self.users = user
          #  self.j = k
    def describe_user(self):
        print("\nUsers information is: ")
        print("\t users frist name is: "+ self.fristname.title())
        print("\t users last name is: "+ self.lastname.title())
        print("\n Users other information are: ")
        for j,k in self.users.items():
            users[j]=k
            print("\t"+j.title()+" : "+ k.title())
    def greet_user(self):
        print("\nHello! "+self.fristname.title()+self.lastname.title())
users={}
user_0 = User('lily','edward',age='16',hometown='beijing')
user_0.describe_user()
user_0.greet_user()
print(users)