
#Ex3: Instance & Static methods in same class
class Sample1:

    def m1(self):
        print("Running instance method m1- Without parameter")

    def m2(self,Name):
        print("Running instance method m2: With parameter- ",Name)

    @staticmethod
    def m3():
        print("Running static method m3- Without parameter")

    @staticmethod
    def m4(Name):
        print("Running static method m4- With parameter ",Name)

s1=Sample1()
s1.m1()
s1.m2("Rahul")
print("----")
Sample1.m3()
Sample1.m4("Amol")
