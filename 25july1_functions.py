# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 08:57:53 2023

"""
#creating a virtual environment
'''
####FOR CREATING VIRTUAL ENVIRONMENT#####
using anaconda navigator
1.Go to environment
2.Go to base(root)
3.open in terminal
  In terminal,write
          >c:/1-python
          >conda create -n testenv1 python=3.9
          #here testenv1 environment is created
          >y
          >conda activate testenv1
(testenv1)>conda list

- To install pandas
        >pip install pandas
   for specific version
        >pip install pandas = version name
        
-If we want to change python version
        >conda install -c anaconda python 3.10
        
-To open spyder
    (testenv1)c:\1-python>spyder
-To open jupyter notebook
    (testenv1)c:\1-python>jupyter notebook
'''

#functions
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "the number is not prime"
            break
    return "the number is prime"

prime_num(5)
print(prime_num(13))
####################
#everytime not need to return value
#it is not necessary to give argument

#below function is without argument
def greet_user():
    #*****display a simple greeting***
    print("hello")
greet_user()

#passing information to a function 
def greet_user(username):
#display a simple greeting
    print(f"Hello,{username}")
    
greet_user('Sanjivani AI')
####
#argument and paremeters

def describe_pet(animal_type,pet_name):
    #animal_name and pet_name are positional argument
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}. ")
describe_pet('Dog','Moti')
#order matters in positional arguments
######
#you can even pass default values
def describe_pet(pet_name,animal_type='Dog'):
    #animal_name and pet_name are positional argument
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}. ")
describe_pet(pet_name='Moti')

#########
#avoiding argument error
def describe_pet(animal_type,pet_name):
    #animal_name and pet_name are positional argument
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}. ")
describe_pet()