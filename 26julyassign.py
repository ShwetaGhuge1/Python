# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:37:01 2023

@author: rohit
"""

'''
-take random 5 no in list and find min and max of list
-take 5 strings in list make it reverse
-take 10 no in list and write script to search for a value(location of no)
-take 10 no in list insert some duplicate no write script to find duplicates
-take vowels in list nd non vowels letters in list find out total no of vowels in list
'''
#take random 5 no in list and find min and max of list
lst1=[1,4,7,3,8]
print("min=",min(lst1))
print("max=",max(lst1))

#take 5 strings in list make it reverse

lst1=['abc','hello','now','engineer']
rev=lst1[::-1]
print(rev)


#o/p:- none

#take 10 no in list and write script to search for a value(location of no)
lst1=[13,4,5,7,8,2,1,9,0,3]
#b=input("enter no to be found:")
print(lst1.index(1))



#take 10 no in list insert some duplicate no and write script to find duplicates
#no.of count of duplicates
lst1=[13,4,5,7,8,2,8,9,4,3]
print(lst1.count(8))

#take vowels in list nd non vowels letters in list find out total no of vowels in list
lst1=['a','y','i','e','h','l','o','v','s','c','b','u']
vowels=0
consonants=0
len(lst1)
for i in range(0,len(lst1)):
    if lst1[i]=='a' or lst1[i]=='e' or lst1[i]=='i' or lst1[i]=='o' or lst1[i]=='u':
        vowels=vowels+1
    else:
        consonants=consonants+1
print("vowels",vowels)
print("consonants",consonants)
    
   