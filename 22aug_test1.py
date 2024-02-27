# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:59:59 2023

@author: rohit
"""

#1
def match_lst(lst1,lst2):
    res=False
    for x in lst1:
        for y in lst2:
            if x==y:
                res=True
            else:
                res=False
    return res
lst1=[1,2,3,4,5]
lst2=[1,6,7,8,5]
match_lst(lst1, lst2)

##############################
def match_lst(lst1,lst2):
    res=False
    for x in lst1:
        for y in lst2:
            if x==y:
                res=True
            else:
                res=False
                return res
lst1=[1,2,3,4,5]
lst2=[1,6,7,8,5]
match_lst(lst1, lst2)

#2

lst1=[2,3,4,5,6]
lst2=[x+6 for x in lst1 ]
lst2


#3
str1='Hello'
str2=str1[::-1]
print(str2)

#4
dict1={1:3,2:4,3:6,5:7,8:9}
for dict_key,dict_value in dict1.items():
        print(dict_key,':',dict_value)
 
#5
dict2={1:3000,2:400,3:6000,5:700,8:9000}
dict3={i:dict1[i] for i in dict1 if dict1[i]>2000 }
dict3

#6
#open file data.txt
filename='data.txt'
with open (filename) as file_object:
    contents=file_object.read()
    print(contents)
    
filename='data.txt'
with open (filename,'r') as file_object:
    print(file_object)
    
#7
#write a python program to construct an infinite iterator 
#that returns evenly spaced values starting with a
#specified number and step
import itertools
start=100
step=10
l=it.count(start,step)



#8
nums=[1,2,3,4,5,6,7,8,9,10]
even_nums=list(filter(lambda x: x%2==0,nums))
print(even_nums)
odd_nums=list(filter(lambda x:x%2!=0,nums))
print(odd_nums)
y= lambda a,b,c:a+b+c
y(1,2,3)


#9
import pandas as pd
import numpy as np
data=({ 'name':['Anna','Dinu','Ramu','Ganu','Emily','Mahesh','Jayesh','venkat','Ajay','Dhanesh'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'atttempts':[1,3,2,3,2,3,1,1,2,1],
        'quality':['yes','no','yes','no','no','yes','yes','no','no','yes']
       })
labels=['a','b','c','d','e','f','g','h','i','j']
df=pd.DataFrame(data,index=labels)
df

#10
#write program to print graph of two or more lines
#and set the line markers

import matplotlib.pyplot as plt
plt.plot([1,2,3,4,3,2,1,2,3,4,3,2,1])
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.show()
