class Sample1:

    num=10

    def m1(self):
        print("running method m1")
        print("method m1 ended")

    def m2(self):
        print("running method m2")
        print("method m2 ended")


#to call function from call need to create object of class
#objectName=className()   -> syntax of object creation
s1=Sample1()                           #className()-> constructor of the class
s1.m1()
s1.m2()
print(s1.num)









