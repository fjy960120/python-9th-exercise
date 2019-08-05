"""一个可以用于表示汽车,电动汽车的类"""
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
