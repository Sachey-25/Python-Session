#for loops
# |  Return an object that produces a sequence of integers
#from start (inclusive) to stop (exclusive) by step
'''print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)

print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)
print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)
print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)
print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)
print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)
print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)
print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)
print("The first 10 numbers are :")
for i in range(0,10):#0 1 2 3 4 5 6 7 8 9
    #I would like to print the first 10 numbers.
    # inside of loop upto the range condition. --- loop
    print(i)'''


'''for i in range(1,10): # 0 1 2 3 4 5 6 7 8 9 
    # print the even and odd number
    # even -- a number %2 == 0 ==> even
    if(i%2==0):
        print(i, "even")
    else:
        print(i, "odd")
for i in range(1,10): #1 2 3 4 5 6 7 8 9 <--- positive.
    if(i==0):
        print("Number is zero")
    elif(i<0):
        print("Negative number")
    elif(i>0):
        print("Positive number")
    else:
        print("Invalid Operation")'''
'''1+2+3+4+5+6+7+8+9+10
3+3 6
10
15
21
28
36
45
55<----- adding first 10 numbers.'''

total=0
for i in range(1,22): # 1 2 3 4 5 6 7 8 9 10
    #print(i+1)# 0 + 1 ==> 2 + 1 ==> 2+1 ==> 3
    # assignment operator
    total +=i  #--> total = i+i;1+1 2 2+2
    print(i) # i values 1 2 3 4 5 6 7 8 9
print("Adding first 20 numbers: ", total)

#nested loops
#----------------
for i in range(0,5):# 0 1 2 3 4 ----> iteration --> rows
    for j in range(0,5):# 0 1 2 3 4 -> value ----> column
        print(i,' ', end='')# newline

print("----------------------------")
#print all even numbers between 1 to 100.
for i in range(1,101): #range(st, end) excusive
    #condition to check even or odd
    # divide ---> quocient
    # modulos ----> reminder : any devides reminder -0
    if(i%2==0):
        print(f"{i} is even")
    else:
        pass #returing pass keyword
        
#Print the sum of all number from 1 to 50.
# 1+2+3+4+5+6+7+8+9+10+.....+50 ==>
sum=0
for i in range(1, 51):
    #1+2+3+4+5+6+7+8+9+10
    #1+2==3 3+3=4+4=8+5=13+6=21+7=28+8=36+9=45+10=55+11=66+12=78+13=91
    #print(sum) # before updating the sum value is 0
    # updating the sum vaue with respect to i; 10= 6+4 
    sum=sum+i
    print(f"{i}+{sum}:", sum)
    
    
        

