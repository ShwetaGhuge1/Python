# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:42:54 2023

@author: rohit
"""

users=['admin','employee','manager','worker','staff']
for user in users:
    if user=="admin":
        print("hello admin,would you like to see a status report")
    elif user=="employee":
        print("hello employee")
    elif user=="manager":
        print("hello manager")
    elif user=="worker":
        print("hello worker")
    else:
        print("hello")

################
#password picker
import string
#pick the adjective
adjectives=['sleepy','slow','smelly','wet',
            'fat','red','orange','yellow','green',
            'blue','purple','fluffy','white','proud',
            'brave']
#pick the nouns
nouns=['apple','dinosour','ball','toaster',
       'goat','dragon','hammer','duck','panda']
import random
adjectives=random.choice(adjectives)
noun=random.choice(nouns)
#select a number
number=random.randrange(0,100)
#select a special character
special_char=random.choice(string.punctuation)
#create the new secure password
password=adjectives+noun+str(number)+special_char
print("your new password is:%s"%password)

#########
#creating multiple passwords
print("welcome to the password picker")
while True:
    adjectives=['sleepy','slow','smelly','wet',
                'fat','red','orange','yellow','green',
                'blue','purple','fluffy','white','proud',
                'brave']
    #pick the nouns
    nouns=['apple','dinosour','ball','toaster',
           'goat','dragon','hammer','duck','panda']

    adjectives=random.choice(adjectives)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password=adjectives+noun+str(number)+special_char
    print("your new password is:%s"%password)
    response=input("would you like to generate new password y or n:")
    if response=='n':
        break
    
##############
#write python code to check strong or weak password
#Strong password conditions
#password has at least 8 characters
#password has one uppercase letter
#password has one lowercase letter
def checkpassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    
#check each character in password 
    for ch in password:
        if ch>='A' and ch<='Z':
            has_upper= True
        elif ch>='a' and ch<='z':
            has_lower= True
        elif ch>='0' and ch<='9':
            has_num=True

    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False

p=input("enter the password:")
if checkpassword(p):
    print("strong password")
else:
    print("weak password")
    
#write program to calculate pizza order bill
'''
small pizza=15
medium pizza=20
large pizza=25
if peporini add small pizza =$2
 peprini for medium or large= $3
extra cheese to any pizza $1
'''
print("Welcome to the pizza hut")
bill=0
pizza=input("which pizza you want to take S,M,L:")
add_pepp=input("do you want to add peporini 'y' or 'n':")
extra_cheese=input("do you want to add extra cheese y or n:")
if pizza=='S':
    print("you need to pay $15 for small pizza")
    bill=15
elif pizza=='M':
    print("you need to pay $20 for medium pizza")
    bill=20
elif pizza=='L':
    print("you need to pay $25 for large pizza")
    bill=25
    
if add_pepp=='y':
    if pizza=='S':
        bill+=2
    else:
        bill+=3
if extra_cheese=='y':
    bill+=1
    
print(f"you need to pay total bill ${bill}")