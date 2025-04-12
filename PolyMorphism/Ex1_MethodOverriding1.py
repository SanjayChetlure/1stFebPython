# ex1: Method Override in Single level Inheritance

#Super class
class Father:
    def car(self):
        print("Car: Swift Desire")

    def money(self):
        print("Money: 1L")

    def home(self):
        print("Home: 2BHK")

#Sub class
class Son(Father):
    def mobile(self):
        print("Mobile: Samsung S20 FE")

    def car(self):              #Method Override
        print("Car: Kia Seltos")

    def money(self):             #Method Override
        print("Money: 1.5L")


print("------Features of Father or super class------")

f=Father()
f.car()
f.money()
f.home()

print("------Features of Son or sub class------")

s=Son()
s.mobile()
s.car()
s.money()
s.home()
