
#Example5.1  -> Global, class , local variables in same example

a,b=10,20       #global variable

class Sample5:

    num1,num2=30,40     #class variable

    def add(self):
        num3,num4=50,60     #local variable

        print(num3+num4)                #addition of local variable
        print(self.num1+self.num2)      #Additiona of class variables
        print(a+b)                      #Additiona of global variable

    def mult(self,c,d):
        print(c*d)
        print(self.num1*self.num2)
        print(a*b)

s5=Sample5()
s5.add()
print("----")
s5.mult(5,6)

