# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:00:51 2023

"""
#lambda function or anonymous function
#very important for interview
#it is hardware perspective

#normal function for addition
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(1,2,3))

#lambda function for addition
add=lambda a,b,c:a+b+c
add(6,5,9)

#here memory is allocated and after giving function
#call the memory is vanished
#memory is allocated for short time while calling function

#lambda function for multiplication
mul=lambda a,b:a*b
mul(3,4)

#for passing arbitrary arguments
#sum() is inbuilt function
#*args = arbitrary argument
val=lambda *args:sum(args)
val(1,2,3,4,5,6)
val(1,4,3,7,5,8,9)

##########
#**args=keyword argument
#two types of argument 1.keyword argument(**data) and 2.non keyword argument(*data)
#when passing keyword argument then result is  in form of dictionary

def person(name,**data):
    print(name)
    print(data)
person(name='Navin',age=28,place='Mumbai',mob_no=987656)
#o/p:- is in form of dictionary

########
def person(name,**data):
    print(name)
    for i,j in data.items():#i for key and j for values
        print(i,j) #data.items() taken for separate output
person(name='Navin',age=28,place='Mumbai',mob_no=987656)
 #o/p: it is not in form of dictionary
      
##############
#lambda function
val=lambda **data:sum(data.values())
#data.values() to assess dictionary values
val(a=2,b=6,c=7,d=10)

##############
max=lambda a,b:a if (a>b)#this is not define properly
print(max(1,2))
#o/p: give error
#########
max=lambda a,b:a if (a>b)else b
print(max(1,2))
print(max(8,10))
print(max(10,2))
#python collection types
#tuples,dictionary,list and set
#tuple:-collection of objects that are ordered and immutable
#immutable - once value defined then not able make any changes afterwords

#creating tuples
tup1=(1,3,5,7)
#accessing elements of tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:\t',tup1[1])
print('tup1[2]:\t',tup1[2])
print('tup1[3]:\t',tup1[3])