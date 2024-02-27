# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:54:50 2023
"""
#1
#write python program to check list is empty

lst=[]
if len(lst)==0:
    print("list is empty")
else:
    print('list is not empty')

#2    
#using list comprehension costruct a list from 
#the squares of each element in list

lst=[1,2,3,4,5]
lst1=[x*x for x in lst]
lst1


#3
#write a script to check whether a given key 
#already exist in dictionary
dict1={1:2,3:4,5:6,7:8}
x=int(input("enter a number"))
if x in dict1:
    print("already exist")
else:
    print("not exist")
#4
#first,create a range from 100 to 160 with step 
#10. second, using dictionary comprehension create
# a dictionary where each number is key and each item 
#divided by 100 is value

dict1={ x:x/100 for x in range(100,160,10)}
dict1


#5
#create a dataframe which comprises of course,fees
#and duration and add tutor column
import pandas as pd
data=({'course':['python','hadoop','java'],
       'Fees':[20000,32000,23000],
       'duration':['34days','43days','54days']})
df=pd.DataFrame(data)
df
df['tutor']=['abc','xyz','lmn']
df

#6
#write dataframe to csv
df.to_csv('data.csv')

#7
#write a python function which returns
# multiple values



#8
#write python which takes two arguments a and b and 
#returns the multiplication of that numbers
a=lambda x,y:x*y
a(4,5)

#9
#write numpy program to test if any of the elements of
#a given array are non zero .

import numpy as np
a=[0,0,3,0,0]
np.any(a)

#10
#write program to display a bar chart of poularity of
#programming languages
#sample data:
#programming languages:Java,Python,PHP,JavaScript,C#,C++
#popularity:22.2,23.7,8.8,8,7.7,6.7


import matplotlib.pyplot as plt
data=pd.Series([22.2,23.7,8.8,8,7.7,6.7],
               index=['Java','Python','PHP','JavaScript','C#','C++'])
data.index
data
fig=plt.figure()
data.plot(kind='bar')
plt.legend()
