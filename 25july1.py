# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 08:57:53 2023

"""
#creating a virtual environment




#Functions
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "the number is not prime"
            break
    return "the number is prime"

prime_num(4)
