
#Super class1
class Sample1:
    def m1(self):
        print("Running method m1 from super class 1-Sample1")

    def m2(self):
        print("Running method m2 from super class 1-Sample1")

#super class2
class Sample2:
    def m3(self):
        print("Running method m3 from super class 2-Sample2")

    def m4(self):
        print("Running method m4 from super class 2-Sample2")


class Sample(Sample1,Sample2):
    def m5(self):
        print("Running method m5 from sub class - Sample")


s=Sample()
s.m5()
s.m1()
s.m2()
s.m3()
s.m4()