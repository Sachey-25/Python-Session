#DataStructures of python
#List : Lists are the storage containers
'''Which can hold elements of any data.
these are hetergenious data, it includes
integers, strings, floats and other lists
List are denoted using [],

example
--------
Listname=[]

Key fetures of Lists
1. Ordered ---> one after next 1,2,3,4,5,6.......
2. Mutable ---> You can modify the list
(add, remove or change the elements)
3. Heterogeneous : A list can contains of different
data types.
4. Dynamic:---> Lists can grow or shrink in size.

list=[1,2,3,4,5,6,7] # static

Dynamic :-- run time
list=input("enter elements")

'''
#Creating a list
#list=[] #empty list

#list with elements
'''list=[2,4,6,8,10]

#List with mixed dataTypes
#list=[23,46,67,"abc",'sachin','shiv','neha',3456.567]

#Nested List
#list=[[1,2,3,45,6],['ABC','abc'],[32.34,675.3]]

#how to access the elements from the list
#---> elements can be accessed using index place.

print(list[0]) # element 2 is present at 0th Index
print(list[1]) # element 4 is present at 1st Index
print(list[2]) # element 6 is present at 2nd Index
print(list[3]) # element 8 is present at 3rd Index
print(list[4]) # element 10 is present at 4th Index.
print("--------------------")
for i in list: #0,1,2,3,4,5,6,7,8...........
    print(i)
list=[3,5,6,67,43,56]
l=[1,2,3,4,5]
for i in l:
    print(i)
print("--------------------")

data=[6,7,8,9,0]
for i in data:
    print(i)
print("--------------------")

my_data=[34,0,2,4,7,89]
for i in my_data:
    print(i)
print("--------------------")

my_list=[56,87,9,143,657,43]
for i in my_list:
    print(i)
print("----------------------")

# accessing the elements of the list
marks=[98,95,92,88,87,85]
#in order to access the elements from list
#with the help of index value, we can get the data.
print(marks[0]) #98
print(marks[1]) #95
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print("-----Negative indexing-----------")

subjects=["Physics","chesmistry","Mathematics","Biology"]
print(subjects[-1])
print(subjects[-2])
print(subjects[-3]) #negative indexing....
print(subjects[-4])
print("---------Positive indexing----------")
print(subjects[0])
print(subjects[1])
print(subjects[2])
print(subjects[3])
print("--------------Index Operator-------------")
print(subjects[0:3]) #the last element is exclusive 0 1 2
print(subjects[0:4]) #here 4th element is exclusive 0 1 2 3
print(subjects[1:4]) #here 4th element is exclusive 1 2 3 
print(subjects[2:4]) #here 4th element is exclusive 2 3
print(subjects[1:3]) #here 3th element is exclusive 1 2

print("----Index Operator with negative indexing--------")
print(subjects[-5:-1]) #end elements is exclusive -1 --> 0
print(subjects[:-1])
print(subjects[:5]) #0 1 2 3 4
print(subjects[::-1])#reverse the list

print("-------Step indexing----------")
print(subjects[0:4:2]) #0  2  4

print("-------Step indexing----------")
numbers=[12,13,21,31,14,41,53,45,6,67,24,45,6,7,89,90]
print(len(numbers))
print(numbers[0:17:2])
print(numbers[0:17:3])
print(numbers[0:17:4])
print(numbers[0:17:5])
print(numbers[0:17:6])
print(numbers[4:17:2])
print(numbers[2:8:3])'''

#List methods
'''1. append(): Adds an element to the end of the list
2. count(): Returns the number of times a specified
element appears in the list
3 copy(): Returns a shallow copy if the list
4.clear(): Removes the number of times a specified element
appears in the list.
5. extend(): Adds element from another list to the end of
the current list
6. index(): Returns the index of the first occurance of
specified currect list
7. insert(): Inserts an element at a specified position
8. pop(): Removes the first occurance of the list element
[or removes the last element if the index not specified]
9. reverse(): Reverse the order of the elements in the
list
10. remove():Removes the first occurance of a specified
element
11. sort():Sorts the list in ascending order (by default)
'''

#----> Data Structures <--- data ---> number,string

list=[] #empty list
#we need to add the element to the empty list
'''#append()'''
# we will use append method in order to add new elements
#to the list, and append() method takes atleast one
#parameter
list.append(10) #item1 : 10
list.append(11)
list.append(12)
list.append(13)
list.append(14)

print("Number list elements")
print(list)
#How to add the strings
list.append('S')
list.append('A')
list.append('C')
list.append('H')
list.append('I')
list.append('N')
print("updated with string elements")
print(list)

list.append(9.34)
list.append(True)
list.append(False)

list.append('RaceCar')

print(list)
print("-----------------")

#Given list
list_numbers=[12,13,14,5,8,20,18,25,27,30]

#sort() # ascending order
list_numbers.sort()
print(list_numbers)

#List to store the even numbers
evenList=[]
#Loop to the lenght of the the given list
for i in list_numbers:
    #check the condition for even numbers
    if(i%2==0):
        #append the values to empty list 
        evenList.append(i)
#print to see the values.
print(evenList)

listPop=[1,5,6,23,89,56,'SACHIN','D','I','N','O', 3.142,455.67,"AB","BA","aabbc","bbred"]
#remove the elements ----> this can be done by two different methods.
# pop() and # remove()
listPop.pop() # without index
print("Last element removed by default since no index")
print(listPop)
listPop.pop() # one more element is popped
print("Last element removed by default since no index")
print(listPop)
print("Last element removed by default since no index")
listPop.pop()
print(listPop)
print("4th element removed index 4")
listPop.pop(4) #element index 4 : 89 should be popped
print(listPop)
print("Last element removed by default since no index")
listPop.pop() # pop() <--- index, without index
print(listPop)
