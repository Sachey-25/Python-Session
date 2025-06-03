#if statement start with keyword if

i=6
#6==6 ??? true,
if(i==6 and i%2==1): #indentation block
    print("i is equals to 6")
    print("this is if statement")
    print("Prints when if statement is true")
#we need to use backspace to come out of the ifblock.
elif(i<5): #false
    print("this is another if block")
    print("this is also executes on true conditon")
    print("we can take multiple number of if blocks")
elif(i==6 and i%2==0):
    print("i is equals to 6")
    print("this is elif statement")
    print("i is not only 6 also devides equally by 2")
else:
    print("Else part")
    print("This is when if expression becomes false")
    print("We can take only one else, that too right next to if statement")

'''I wanted to check the given number is even or odd.
---------------------------------------------------
A number which devides eqaully by 2 and whose reminder
is 0.
that number is called even number. and whose reminder is 1
that number is odd.'''
num=int(input('Enter a number: '))
if(num%2==0):
    print(f"Even number: {num}")
else:
    print(f"Odd number: {num}")



    


    
