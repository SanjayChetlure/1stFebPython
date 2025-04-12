
#Ex4: class variable & use of self keyword
class Sample4:
    num1=10     # class variable -> variable which is declared inside class
    num2=20

    def add1(self):
        print(self.num1+self.num2)

    def add2(self):
        num3=30                             #local variable
        print(self.num1+self.num2+num3)

    def add3(self,num4):                    #num4= local variable
        print(self.num1+self.num2+num4)

    def mult(self):
        print(self.num1 * self.num2)

s4=Sample4()
s4.add1()
s4.add2()
s4.add3(50)
s4.mult()


