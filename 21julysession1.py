# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 14:21:04 2023

@author: rohit
"""

#print Hello world
print('Hello world') 

#Variables
#Types of Numbers
#There are three types used to represent of numbers in python
#these are integers types,floating point numbers and complex numbers.

x=1
print(x)
print(type(x))
x=10000000000000000000000000000000000000000000001
print(x)
print(type(x))

#the input function always return a string
'''
If we want to ask user to input an integer number,
then we will need to convert the string returned 
'''
#by default python takes any input as string
age=input('enter your age:')
print(type(age))
print(age)

age1=input('enter your age:')
print(type(age1))
print(age1)

age2=input('enter your age:')
print(type(age2))
print(age2)
age=age1+age2
print(age)

#age as integer input
age=int(input('enter your age:'))
print(type(age))
print(age)

age1=int(input('enter your age:'))
print(type(age1))
print(age1)

age2=int(input('enter your age:'))
print(type(age2))
print(age2)
age=age1+age2
print(age)

###################################################
#floating point Numbers
'''Real numbers ,or floating point numbers
are represented in python using IEEE 754
double-precision binary floating point number format

'''
exchange_rate=1.83
print(exchange_rate)
print(type(exchange_rate))

##########################
int_value=100 #you can also write a=100 
string_value='1.5'
float_value=float(int_value)
print('int value as a float:',float_value)
print(type(float_value))
float_value=float(string_value)
print('string value as a float:',float_value)
print(type(float_value))

#############################
#Complex Numbers
c1=1
c2=2j
print('c1:',c1,',c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#############################
#Boolean Value
#python supports anotheer type called boolean
#a Boolean type can only be one of True or False
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

###############################
#convert string to boolean
#either string contain True or False (and nothing else)
status=bool(input('OK it is confirmed?:'))
print(status)
print(type(status))

########################################
#Arithmetic Operators
'''

'''
home=10
away=15
print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))

goals_for=10
goals_against=7
print(goals_for-goals_against)
print(type(goals_for-goals_against))
##################################
#this / operator gives actual division i,e. in form of float
print(100/20)
print(type(100/20))
#####3
#this // operator gives division in integer format
print(100//20)
print(type(100//20))

####
#this % operator gives remainder
print('Modulus division 100%13:',100%13)
print('Modulus division3%2:',3%2)

#######
#this ** operator is used for indexing
a=5
b=3
print(a**b)
#assignment operators

x=0
x+=1 #has the same behaviour as x=x+1
######################
#None Value
winner =None
print(winner is None)
##
print(winner is not None)

#None
winner=None
print('winner:',winner)
print('winner is None:',winner is None)
print('winner is not None:',winner is not None)
print(type(winner))
print('Set winner to True')
winner=True
##########################
#flow of control using If statements
num = int(input('enter a number:'))
if num>0:
    print(num)
    
num = int(input('enter a number:'))
if num>0:
    print(num)

num = int(input('enter a number:'))
if num<0:
    print('its negative ')
else:
    print('Its not negative')

#the use 

