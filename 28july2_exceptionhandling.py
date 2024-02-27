# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:11:26 2023

"""
#the error signifies a situation that mostly
#happens due to the absense of system resources.
#the exceptions are the issues that can appear
#at runtime and compile time.
#It majorly arises in the code or program
#authored by the developers.

#there are two concepts:- error and exception
#error:-due to absence of system resources
#exception :- appear at runtime or at compile time
#you can handle exception but not error

#exceptions are handled with try-except block

#handling the zerodivision error exception

#
print(5/0)

#using try-except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")
    
##using exception to prevent crashes
#
#this below code not executed because of exception handling
a=5
b=6
c=a=b
print(5/0)
print(c)

#o/p:- gives error

#by using exception handling above code will be
a=5
b=6
c=a+b
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")
    
print(c)

#handling the FilenotFoundError Exception
filename='alice.txt'
with open(filename,encoding='utf-8') as f:#name of file object is 'f'
    contents=f.read()
######
# exception handling files for above code 
#encoding is important
filename='alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print(f"Sorry,the file {filename} does not exist.")
#############

#Storing data

#json-javascript object notation
#the JSON format was originally developed for 
#javascript
#using json.dump() and json.load()
#json.dump()- takes json object and returns a string
#json.loads()-takes a string and returns a json object
#json files
import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)
    
################
#saving data with json is useful
#when you are working with user-generated data
import json
username=input("What is your name?")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username,f)
print(f"we'll remember you when you come back,{username}!")
###########
#now let's write new program that greets
#a user whose name has already been stored
import json
filename='username.json'
with open(filename) as f:
    username=json.load(f)
print(f"Welcome Back,{username}!")

#we need to combine both program in one code
#load username if it has been stored previously
#otherwise , prompt for the username and store it.
filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("what is your name?")
    with open(filename,'w') as f:
        json.dump(username,f)
    print(f"we'll remember you when you come back,{username}!")
else:
    print(f"welcome back,{username}!")

