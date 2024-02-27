1# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:37:59 2023

@author: rohit
"""

#python collection types
#tuples,dictionary,list and set are data structures in python
#tuple:-collection of objects that are ordered and immutable
#immutable - once value defined then not able make any changes afterwords
#tuples are used to store multiple items in a single variable
#tuples used to store collection of data
#tuple is a collectin which is ordered and immutable
#tuples are written with round bracket ()
#tuples can hold diff datatypes
#creating tuples
tup1=(1,3,5,7)
#accessing elements of tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:\t',tup1[1])
print('tup1[2]:\t',tup1[2])
print('tup1[3]:\t',tup1[3])
########
#tuple consist diff datatypes
tup2=(1,'John',True,-23.45,10.11)
print(tup2)

#iterating over tuples
tup3=('apple','orange','plum','apple')
for x in tup3:
    print(x)
    
#tuple related functions
#find out length of tuple
len(tup3)

#how many times a specified value is appears in a tuple
tup4=('apple','orange','plum','apple','apple')
#tuple allows duplicate values
tup4.count('apple')

#you can also find out (first) index of a value in a tuple
print(tup4.index('apple'))
print(tup4.index('plum'))

#checking if an element is exist
if 'orange' in tup3:
    print("orange is in tuple")
    
#holypython.com
#hackerrank

#nested tuples
#tuples can be nested within tuples
#that is a tuple can contain, as one of its
#elements,another tuple.
tuple1=(1,3,5,7)
tuple2=('john','denise','phoebe','adam')
tuple3=(42,tuple1,tuple2,5.5)
print(tuple3)

#it is not possible to add or remove
#elements from a tuple;they are immutable


###########################
#List#
#it is mutable,ordered,[] brackets
#mutable- you can add or delete elements
#creating lists
list1=['john','paul','george','ringo']
#we can have nested lists and list contains diff datatypes
lst1=[1,43.5,True]
lst2=['apple','orange',31]
root_list=['john',lst1,lst2,'denise']
print(root_list)

#accessing elements from list
lst1=['john','paul','george','ringo']
print(lst1[-1])
lst1[0]
lst1[-3]
#in nlp and advance nlp list is used

lst1=['john','paul','george','ringo']
print('lst1[1]',lst1[1])
print('lst1[-1]',lst1[-1])
print('lst1[1:3]',lst1[1:3])
print('lst1[:3]',lst1[:3])
print('lst1[1:]',lst1[1:])

################
#adding to a list
lst1=['john','paul','george','ringo']
lst1.append('pete')
print(lst1)

#you can also add all items in list
lst1=['john','paul','george','ringo']
print(lst1)
lst1.extend(['albert','bob'])
print(lst1)

#inserting into a list
a_list=['john','paul','george','ringo']
print(a_list)
a_list.insert(1,'paloma')
print(a_list)


#list concatenation
lst1=[2,4,5]
lst2=[3,7,8]
lst3=lst1+lst2
print(lst3)

#assignment
'''
-take random 5 no in list and find min and max of list
-take 5 strings in list make it reverse
-take 10 no in list and write script to search for a value(location of no)
-take 10 no in list insert some duplicate no write script to find duplicates
-take vowels in list nd non vowels letters in list find out total no of vowels in list
'''