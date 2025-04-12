
#Ex1: Instance method  (non-static method)
class Sample1:

    def m1(self):
        print("Running method m1- Without parameter")

    def m2(self,Name):
        print("Running method m2: With parameter- ",Name)

    def m3(self):           #Method with no implementation
        pass

s1=Sample1()                #step1: create object of class     ->  objName=className()
s1.m1()                     #step2: method call -> objName.methodName()
s1.m2("Ganesh")
s1.m3()

