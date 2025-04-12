#StartNum=2
#EndNum=8
#incr/decr=incr 2

print("-----print even num 2 to 8-----")
for i in range(2,9,2):     #2+2=4+2=6+2=8+2=10   -> 10<9
    print(i)               # 2 4 6 8

print("----------print even num from 10 to 50----------")
for i in range(10, 51, 2):
    print(i)

print("---------table of 5-----------")
for i in range(5, 51, 5):
    print(i)

print("---------table of 5-----------")
for i in range(1,11):
    print(i*5)

print("---------print square of num from 5 to 10-----------")
for i in range(5,11):   #6    6<11
    print(i*i)   #6*6=36