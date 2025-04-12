class Sample1:
    def m1(self):
        print("Running method m1 from super class")


class Sample2(Sample1):
    def m1(self):
        super().m1()
        print("Running method m1 from sub class")

s2=Sample2()
s2.m1()