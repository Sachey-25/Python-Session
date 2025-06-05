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
list=[2,4,6,8,10]

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
print(numbers[2:8:3])
