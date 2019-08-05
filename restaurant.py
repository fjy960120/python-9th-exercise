class Resaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisinetype = cuisine_type
    def describe_restaurant(self):
        print("\nThis restaurant's name is : "+ self.name.title())
        print("The restaurant's cuisine type are : "+self.cuisinetype.title())
    def open_restaurant(self):
        print("This reataurant is openning!")
