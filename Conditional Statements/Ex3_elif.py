
marks=62

#30>=65
if marks>=65:
    print("Distinction")
elif marks>=60 and marks<65:   #30>=60  and 62<64 = true           # 60 to 64 -> 1st class
    print("1st class")
elif marks>=50 and marks<60:  #30>=50 and 58<60
    print("2nd class")
elif marks>=35 and marks<50:  #30>=35 and 43<50
    print("pass")
elif marks<35:                #30<35
    print("Fail")


print("program ended")

# true and true = true
# true and false = false
# false and true = false
# false and false =false