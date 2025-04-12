
#Super/Parent/Base class
class Father:
    def car(self):
        print("Running car method from super class")

    def money(self):
        print("Running Money method from super class")

    def home(self):
        print("Running Home method from super class")

#Sub/Child class
class Son(Father):
    def mobile(self):
        print("Running mobile method from sub class")

    # def car(self):
    #     print("Running car method from super class")
    #
    # def money(self):
    #     print("Running Money method from super class")
    #
    # def home(self):
    #     print("Running Home method from super class")


s=Son()
s.mobile()
s.car()
s.money()
s.home()
