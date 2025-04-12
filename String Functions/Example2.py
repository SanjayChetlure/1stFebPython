s1="abc"
s2="xyz"
s3="  abcd   "
s4="my name is abc"

print(s1+s2)      #abcxyz

print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())

print(s4.replace("abc","xyz"))    # my name is xyz

print("------------------")

s5="velocity"
s6="ABcd"
print(s5.capitalize())      #Velocity      convert 1st letter of string to upper case
print(s4.title())           #My Name Is Abc
print(s6.swapcase())        #abCD

print("----------")

str1="123"
str2="abc123"
str3="  "
str4="my name is abc is abc is"

print(s5.isalpha())             #True
print(str1.isdigit())           #True
print(str2.isalnum())           #True
print(str3.isspace())             #True

print(str4.count("abc"))





