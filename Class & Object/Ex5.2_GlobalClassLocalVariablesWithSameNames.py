
#Example5.2  -> Global, class, local variables with same name in same example
a,b=10,20           #global variables

class Sample5:

    a,b=30,40           #class variables

    def add(self):
        a,b =50,60          #local variables
        print(a+b)               #50+60=110 add local variables
        print(self.a+self.b)     #30+40 =70 add of class variables
        print(globals()['a']+globals()['b'])  #10+20=30  add of global variables

s5=Sample5()
s5.add()