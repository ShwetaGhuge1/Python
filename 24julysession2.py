# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:09:43 2023


"""
##leap year code
def is_leap_year(year):
    if((year>0) and (year%4==0)and(year%100==0)and(year%400==0)):
        return True
    return False

print(is_leap_year(1600))

##
##palindrome number
def is_palindrome(input):
    if input=="":
        return "you entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
        #remaining code
        
#mario Pyramid important question
'''
****
***
**
*
'''
#box of 4X4 '*' or'#'

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
'''
output
# # # #
# # # #
# # # #
# # # #
'''

#####
for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()
'''
output
# 
# # 
# # # 
# # # #
'''
###########
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
'''

Mario Pyramid

output:-
# # # # 
# # # 
# # 
# 
'''
###prime number
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "the number is not prime"
            break
    return "the number is prime"
prime_num(17)

############session 2 #######

x,y,z=5,6,7
print(x)
print(y)
print(z)

x,y,z=5
print(x)
print(y)
print(z)

###global variable
## global variable can be access 
#everywhere in code but not local variable

x="awesome" #global variable
def my_function():
    print("python is "+x)
my_function()
##

##global and local variable
x="awesome" #global variable
def my_function():
    x="fantastic" #local variable
    print("Python is "+x)
my_function()
print("Python is "+x)

######
#Dictionary
#it is type of declaration in python
#dictionary contains key-value pair
x={"name":"ram","age":34}
print(type(x))
######

#############
#concatenation of string 
#and integers is not allowed
str1="hello"
str2=2
str3=str1+str2
print(str3)
#here you will get error:can only concatenate str (not "int") to str

######
#String
#if you want multiple strings
x="""This is python.
It is very powerful"""
print(x)

##########
#string slicing
x="This is python.It is very Powerful."
print(x[2:10])
#[i:j]slicing is done from ith index 
#to j-1th index

######
#slice from start
x="This is python.It is very Powerful."
print(x[:3])

#slicing to the end
x="This is python.It is very Powerful."
print(x[4:])

#negative indexing
#it is in '<-' direction i,e,in opposite direction
x="This is python.It is very Powerful."
print(x[-5:-2])

#################
#modify String
#string functions

#capitalize string
x="This is python.It is very Powerful."
print(x.upper())

x=x.upper()
print(x.lower())

####################
#Remove white space,remove 
#white space from initial to end
x="       This is python"
print(x.strip())
#######
#replace the word
x="Hello World"
print(x.replace("Hello","Gello"))

#use of split which replaces white space/or
x="Hello,world"
print(x.split(","))
## output:-['Hello', 'world']--this is vectorization in form of list

#
x="Hello world"
print(x.split(" "))

############
#find function
x="This is python and It is very Powerful."
print(x.find("and"))

############
#for reversing string
x="Hello World"
string1=x[::-1]
print(string1)

#
x="Hello World"
string1=x[::-2]
print(string1)

#############
#find method searches for specified value
# and returns the position
x="This is python and It is very Powerful."
print(x.find("and"))

#String concatenation
x="hello"
y="world"
print(x+y)
##########
#to add white space
print(x+" "+y)

##################
#String format
x=36
y="my name is Anthony"
# print(x+y)
# it will give error
print(f"my name is Anthony and my age is {x}")
#this method i,e. print(f"....") is called number manipulation and fstring in python
#number manipulation using fstring

#########
#if you want to display multiple numbers in a single string
quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and item number is {item_no}, price is {price}")

###################
#other method for using numbers in a string
quantity=3
item_no=54
price=67
my_order="I want {} pieces and item number is {},its price is {}"
print(my_order.format(quantity,item_no,price))

###########
#we are giving here argument number in curly braces
quantity=3
item_no=54
price=67
my_order="I want {0} pieces and item number is {1},its price is {2}"
print(my_order.format(quantity,item_no,price))

###########
#use of escape character
#escape character allows you to use double quates when you normally would
text="This is fun fair and it has big \"round rigo\""
#text="This is fun fair and it has big "round rigo""
#this will give error
print(text)
###########
a=20
b=10
print(a!=b)
#
#operator precedence
print(3*3+3/3-3)
#o/p:-7
