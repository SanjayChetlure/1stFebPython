PEM=550

#  550>=500
if PEM>=500:                                #outer if
    print("Selected for Mains Exam")
    print("Preparing for mains exam")
    MEM=800
    if MEM>=1000:     #1200>1000            #nested if  or inner if
        print("Got selected")
    else:
        print("Rejected from mains exam - MEM<1000")
else:
    print("Rejected from PE - PEM<500")

print("program ended")