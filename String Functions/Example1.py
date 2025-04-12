
s1="velocity"
s2="ABCD"
s3="abcd"
s4="my name is abc"
s5="abcaba"             #   0-5



print("-------")
print(s1[3])            # o
print(s1[2:5])          # 2-4  #s1[startIndex:endIndex+1]

print(s5.find('b'))          # returns index of 1st occurrence chars
print(s5.index('b'))         # Alternate way

print(s5.rfind('b'))          # returns index of last occurrence chars
print(s5.rindex('b'))         # Alternate way
print("----------")
print(len(s1))

# s1=s1.upper()       #Re-Initialization
# print(s1)
print(s1.upper())
print(s1)

# s2=s2.lower()
# print(s2)
print(s2.lower())
print(s2)

print(s2==s3)                        #compare data & case
print(s2.__eq__(s3))                #compare data & case        #Alternate way
print(s2.lower()==s3.lower())        #compare only data

print("--------")

print("is" in s4)
print(s4.__contains__("is"))  #Alternate way

print(s4.startswith("my"))
print(s4.endswith("Abc"))

