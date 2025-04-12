
# def addition(num1, num2):
#     print(num1+num2)

#Without return type
# def addition(num1, num2):
#     sum=num1+num2
#     print(sum)
#
# addition(10,20)         #30

print("-------Function with 1 return statement-------")
def addition(num1, num2):
    sum=num1+num2
    return sum

num=addition(10,20)         #30
print(num)
print("----")
print(addition(10,20))

print("-----------------------------")

def getStudentName():
    name="Amol"
    return name

SName=getStudentName()
print(SName)
print("----")
print(getStudentName())






