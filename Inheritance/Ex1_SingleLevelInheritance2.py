
class Father:

    num1=10          #class variable from super class

    def car(self):
        print("Running car method from super class")

    def money(self):
        print("Running Money method from super class")

    def home(self):
        print("Running Home method from super class")


class Son(Father):

   # num1 = 10  # class variable from super class
    num2=20         #class variable from sub class

    def mobile(self):
        print("Running mobile method from sub class")

    def add(self):
        print(self.num2+self.num1)



s=Son()
s.mobile()
s.car()
s.money()
s.home()
s.add()
