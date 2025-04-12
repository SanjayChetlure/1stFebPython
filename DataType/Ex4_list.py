ls = [6,5,0,"abc",11.5]         #index start from 0


print("------Print all data--------")
for i in ls:
    print(i)

print("------------------------")

ls[3]="ABC"

#find length of list
print(len(ls))      #5

#get data from specific index
print(ls[1])

#verify any specific data available in list
print(ls.__contains__(6))

print(ls)

#add element
ls.append(4)
print(ls)

#add multiple elements
ls.extend([-5,-6])
print(ls)

#add element to specific index
ls.insert(3,10)
print(ls)


#remove element by index
ls.pop(1)
print(ls)

ls.pop()        #remove ele from last index
print(ls)

ls.remove(11.5)
print(ls)

#copy list
ls1=ls.copy()
print(ls1)

print("------------sorting-------------")

ls2=[3,1,4,2]
print(ls2)

#Ascending order
ls2.sort()     #[1,2,3,4]
print(ls2)

#Descending order
ls2.reverse()
print(ls2)

#sort info without changing original data
ls3=sorted(ls2)
print(ls3)

print("----------------")
lst3=[1,4,8,6,4,6,2,8,8]
print(lst3.index(8))
print(lst3.count(1))


lst3.clear()
print(len(lst3))


del lst3
print(lst3)



