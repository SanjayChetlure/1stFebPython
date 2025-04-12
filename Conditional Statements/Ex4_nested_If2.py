shoppingAmount=7000

#   700>=500
if shoppingAmount>=500:                  #outer if
    print("free delivery")
    if  shoppingAmount>=5000:            #7000>=5000   #inner/nested if
        print("Additional 10% discount")
    else:
        print("No Additional discount")
else:
    print("delivery charges: 50rs")