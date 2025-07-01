#List methods
'''
1. append()
2. extend()
3. insert()
4. remove()
5. copy()
6. count()
7. pop()
8. reverse()
9. sort()
10. clear()
11. index()
'''

#append()
#Method adds an item to the end of the list.
'''languages=['C','C++','Java','Python','Csharp']
semiconductor=['registers','capaciters','trasistors','diodes']
marks=[123,98,97,86,95,94]
subjects=['Kan','Eng','Hin','Maths','Sci','So-Sci']

#select any list from above and make add anywhere

semiconductor.append('Mux') #one parameter
print(semiconductor)
semiconductor.append('LogicGate')
print(semiconductor)

emptyList=[]
emptyList.append('example1')
emptyList.append(12)
emptyList.append('ABCD')
emptyList.append('example2')
emptyList.append(32)
emptyList.append('WXYZ')
print(emptyList)

2. Extend() : The Extend() method **adds all the items** of the
specified iterable, such as list, tuple, dictionary or string
to the end of a list.

#list1 extend to list2
#list2 extend to list1
#marks.extend(subjects) #marks extended to subjects.
#subjects.extend(marks) #subjects extened to marks.

evenList=[] #empty list for even numbers
oddList=[] #empty list for odd numbers
evenList.append(2)
evenList.append(4)
evenList.append(6)
evenList.append(8)
print(evenList)
print("-------------------------")
oddList.append(1)
oddList.append(3)
oddList.append(5)
oddList.append(7)
print(oddList)

print("Even and odd elements in oneList")
oddList.extend(evenList)

#before . operator whichever the list is taken that list will
#be impacted with its elements.
print(oddList)

evenList.extend(oddList)
print(evenList)

#3. Insert() : Method inserts an element to the list at the
#specific index.(position)
vowels=['A','I','U'] #AEIOU sorted -- increasing order

print("Before insert, vowles are : ", vowels)
#lets make complete elements of vowels.
#append() ---> adds to the last
#extend() ---> adds to the last
#insert:
#syntax : insert(<indexValue>,<elementValue>)

vowels.insert(1,'E')
vowels.insert(3,'O')
print("After insert, vowels are: ", vowels)

#4. remove() : The remove method removes the matching
#element which is passed as parameter from the list.
#Syntax : remove(<elementValue>)
evenList.remove(2) #values : Value must present in the applied List
evenList.remove(4)
evenList.remove(6)

print(evenList)
print(oddList)'''

numbers=[2,3,5,7,9,24,11,30,45,43,13,17]
#Given list contains few numbers perform appropriate action
#and display only prime number in seperate list.
primeNumbers=[]

#prime numbers are the numbers, which divides by itself or by 1
#below numbers should be removed from the list. 
numbers.remove(9)
numbers.remove(24)
numbers.remove(30)
numbers.remove(45)
#Updated list
primeNumbers.append(numbers)
print('Updated list of primenumbers: ', primeNumbers)



