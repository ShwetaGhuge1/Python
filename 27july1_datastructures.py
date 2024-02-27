# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:14:15 2023

"""
#removing from a list
#it is use for web scrapping
another_lst=['Gary','mark','Robbie','Jason','Howard']
print(another_lst)
another_lst.remove('Robbie')
print(another_lst)

#####
#pop () method
#it removes an element from list
#in pop method you have to give index of entity which is 
#been removed while in remove method you have to give element 
#which we want to remove
another_lst=['Gary','mark','Robbie','Jason','Howard']
print(another_lst)
print(another_lst.pop(2))
print(another_lst)

#inserting into list
another_lst=['Gary','mark','Robbie','Jason','Howard']
print(another_lst)
another_lst.insert(1,'paloma')
print(another_lst)
######


#####CREATING A SET############
#set is unordered
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)
for item in basket:
    print(item)
    
#############
#adding items to set
basket={'apple','orange','banana'}
basket.add('apricot')
print(basket)

###########
#more than one element
basket={'apple','orange','banana'}
basket.update(['apricot','mango','grapes'])
print(basket)


#############
#obtaining length of set
basket={'apple','orange','banana','apple','orange','apple','pear','orange'}
print(len(basket))

#######
#obtaining max and min values inset
basket={1,4,7,9,33,78,2,0}
print(max(basket))
print(min(basket))

#removing an item
basket={'apple','orange','banana','apple','orange','apple','pear','orange','apricot'}
print(basket)
basket.remove('apple')
basket.discard('apricot')
print(basket)

##############
#Set Operations
s1={'apple','orange','banana'}
s2={'grapefruit','lime','banana'}
print("union:",s1|s2)
print('intersection',s1&s2)
print('difference',s1-s2)
###############

#Dictionaries
#it is a set of association
#it consist of key-value pair
#changeable(mutable) and indexed

Capitals={'Maharashtra':'Mumbai','Gujrat':'Ahmedabad',
        'UP':'Lucknow','Karnataka':'Bangolore',
        'Andhrapradesh':'Hyderabad'}
print(Capitals)

#Accessing via keys
print('Capitals[Maharashtra]:',Capitals['Maharashtra'])

#Adding a new entry
Capitals['West Bengal']='Kolkata'
Capitals

#changing a keys value
Capitals['Gujrat']='Gandhinagar'
print(Capitals)

#removing an entry
Capitals.pop('Karnataka')
print(Capitals)
#other method of removing entry
del Capitals['UP']
print(Capitals)

#iterating over keys
Capitals={'Maharashtra':'Mumbai','Gujrat':'Ahmedabad',
        'UP':'Lucknow','Karnataka':'Bangolore',
        'Andhrapradesh':'Hyderabad'}
#to access keys
for states in Capitals:
    print(states,end=',')

#to access keys and values
for states in Capitals:
    print(states,end=',')#to access keys
    print(Capitals[states])#to access values

#values,keys and items
print(Capitals.values())
print(Capitals.keys())
print(Capitals.items())

######
#checking key membership
print('Karnataka' in Capitals)
print('Bihar' not in Capitals)

#length of dictionary
print(len(Capitals))

#Dictionaries can have values in tuple
seasons={'Summer':('Feb','Mar','Apr','May'),
         'Rainy':('June','July','August','Sept'),
         'Winter':('Oct','Nov','December','January')}
print(seasons['Rainy'])
print(seasons['Rainy'][0])

#dictionary methods
#get() is a useful method to access the values
#of a key in a dictionary.
print(Capitals.get('UP'))

###
#dictionary cannot have two items with same key
dict2={"brand":"Maruti",
       "model":"Breeza",
       "year":2021,
       "year":2020}
print(dict2)

#Loop through dictionary,it will show only keys
for x in dict2:
    print(dict2[x])

#you can also use the values() method to return values 
#of dict2