
#Ex1: Method Over loading
class Sample1:
    def add(self,a=0,b=0,c=0,d=0):
        print(a+b+c+d)

s1=Sample1()
s1.add()
s1.add(10,20)
s1.add(10,20,30)
s1.add(10,20,30,40)


print("-------")


class Sample2:
    def printName(self,name="xyz"):
        print(name)

s2=Sample2()
s2.printName()
s2.printName("Amol")




