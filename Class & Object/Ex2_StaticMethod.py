
#Ex2: static method
class Sample1:

    @staticmethod          #staticMethod -> Annotation
    def m4():               #no need to mention self keyword for staticMethod
        print("Running static method m4 - Without parameter")

    @staticmethod
    def m5(Name):
        print("Running static method m5 - With parameter ",Name)

Sample1.m4()        #ClassName.methodName()
Sample1.m5("Rahul")
