#Ex2: With parameter constructor
class Demo1:

    #use1: initialize variables
    #use2: initialize object(copy all data from class to object)
    def __init__(self,Name,rollNum):             #With parameter constructor
        print("Running With parameter constructor ")
        print("Name: ",Name)
        print("RollNum: ",rollNum)

    def m1(self):
        print("Running method m1")

d1=Demo1("Rahul",101)                # className() -> Demo1() -> constructor call

