# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:10:10 2023

"""
#returning dictionary
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('Ram','Sarkar')
print(musician)

############
#passing list or return list
def greet_users(names):
    for name in names:
        msg=f"hello,{name.title()}"
        print(msg)
username=['sanket','Saurabh','Surabhi']
greet_users(username)
    #name.title() is capitalize first letter
    
##########
#passing arbitrary number of arguments
def make_pizza(*toppings):
    #pass the list of toppings that have been requested
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#Now we can replace the print() call with a loop that
#runs through the list of toppings and describes the 
#the pizza being ordered

############
#the diff between above and this code is only
#in form of output
#output in vertical form 
def make_pizza(*toppings):
    print("Making a pizza with following toppings")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

###############
#mixing positional and arbitrary arguments
def make_pizza(size,*toppings):
    print(f"making a pizza {size} inch with following toppings")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

##############
#importing the code from another file (here pizza.py)
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

################
#importing specific functions
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

###################
#using as to give a functions as alias
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

##############
#using as to give a module an alias
import pizza as p
p.make_pizza(16,'pepperoni' )
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

#####################
#importing all functions in a module
from pizza import *
make_pizza(16,'pepporini')
make_pizza(12,'mushrooms','green peppers','extra cheese')

###################
#scope of variable
x=x+1
x=6
print(x)
#o/p:-give error
#
x=6
x=x+1
print(x)
#o/p:-7
###########

