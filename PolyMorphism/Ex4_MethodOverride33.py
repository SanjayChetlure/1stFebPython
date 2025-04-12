class Sample1:
    num1=10
    num2=20

    def arithMaticOperation(self):
        print(self.num1+self.num2)


class Sample2(Sample1):

    def arithMaticOperation(self):
       super().arithMaticOperation()
       print(self.num1*self.num2)

s2=Sample2()
s2.arithMaticOperation()

