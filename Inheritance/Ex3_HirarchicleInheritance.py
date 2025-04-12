#Ex3:Hierarchical Inheritance:

#Super class
class Father:
    def car(self):
        print("Running car method from super class")

    def money(self):
        print("Running Money method from super class")

    def home(self):
        print("Running Home method from super class")


class Son1(Father):
    def mobile(self):
        print("Mobile method from Son1")


class Son2(Father):
    def laptop(self):
        print("Laptop method from Son2")

print("--------Features of Son1-----")
s1=Son1()
s1.mobile()
s1.car()
s1.money()
s1.home()

print("--------Features of Son2-----")
s2=Son2()
s2.laptop()
s2.car()
s2.money()
s2.home()