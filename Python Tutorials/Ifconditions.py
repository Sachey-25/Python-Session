num=10
i=num%2 #true
if(i):  # boolean expression  -- False, True
    pass #pass returns a null operation.
    print("if block", i)
elif(True):
    print("Elif block")

#global sentence.
print("out of if block",i)

busticket=int(input("Enter the ticket amount"))
if(busticket==10 and busticket<=50):
    print("travelling can travel upto 8km")
elif(busticket==20 and busticket>100):
    print("Travel time is 10 mins to 2hrs.")
elif(busticket==30 and busticket>150):
    print("Travel time is 30mins to 3grs")
else:
    print("Operatoion is invalid")

numberO=int(input("Fitst number"))
operation=input("Selete the operation: +,-,*,/,")
numberT=int(input("Second number"))
if(operation=='+'):
    print(numberO+numberT)

