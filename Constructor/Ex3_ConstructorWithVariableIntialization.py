
#Ex3: Constructor with variable initialization

class Sample1:

    def add(self,num1, num2):
        print(num1+num2)

    def mult(self, num1, num2):
        print(num1 * num2)

    def sub(self, num1, num2):
        print(num1 - num2)

s1=Sample1()
s1.add(10,20)
s1.mult(10,20)
s1.sub(10,20)

print("--------------------------")

class Sample2:

    def __init__(self,num1, num2):
       self.a=num1       #10                      #convert/assign local variable into class variable
       self.b=num2       #20

    def add(self):
       print(self.a+self.b)

    def mult(self):
        print(self.a*self.b)

    def sub(self):
        print(self.a-self.b)

s2=Sample2(10,20)
s2.add()
s2.mult()
s2.sub()

print("---")

s3=Sample2(5,6)
s3.add()
s3.mult()
s3.sub()

