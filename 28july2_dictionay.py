# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:42:27 2023


"""
#write a program to add key to a dictionary
d={0:10,1:20}
print(d)
d.update({2:30})
print(d)

##
d={0:10,1:20}
print(d)
d[2]=30
print(d)

# write python script to concatenate the following dictionaries
#to create new one:
   # Sample dictionary:
'''
       dict1={1:10,2:20}
       dict2={3:30,4:40}
       dict3={5:50,6:60}
       Expected result: {1:10,2:20,3:30,4:40,5:50,6:60}
'''
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict4={}
for d in (dict1,dict2,dict3):dict4.update(d)
print(dict4)

##################
#write program to check whether a given key is 
#already exist in dictionary
d={1:10,2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print("key is present in dictionary")
    else:
        print("key is not present in dictionary")
is_key_present(5)
is_key_present(8)

##################
#write program to iterate over dictionaries using for loops
d={'x':10,'y':20,'z':30}
for dict_key,dict_value in d.items():
    print(dict_key,':',dict_value)
#############
