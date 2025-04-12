
#Ex1: Without parameter constructor
class Demo:

    #use1: initialize variables
    #use2: initialize object(copy all data from class to object)
    def __init__(self):             #Without parameter constructor
        print("Running Without parameter constructor")

    def m1(self):
        print("Running method m1")

d=Demo()                # className() -> Demo() -> constructor call

