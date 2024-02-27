# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:00:06 2023
"""
#stackoverflow and github
#data structures
########

#write python program to add all items in list
def sum_list(items):
    sum=0
    for i in items:
        sum=sum+i
    return sum
        
lst=[2,7,4,3,-1]
print(sum_list(lst)) #or print(sum_list([1,4,6,-7]))

#write python program to multiply all the items in list
def mul_list(lst):
    mul=1
    for i in lst:
        mul=mul*i
    return mul

print(mul_list([6,-8,-5]))

#write python program to find largest number in list
lst=[6,4,22,8,9]
print("largest number=",max(lst))

def max_num_in_list(lst):
    max=list[0]
    for a in lst:
        if a>max:
            max=a
    return max

print(max_num_in_list([1,2,4,-8,0]))
#not give output error generated

########################################
#write program to print smallest number
lst=[13,8,4,0,-5]
print('smallest number',min(lst))

#write python program to count the number of strings which 
#satisfies that the string length is 2 or more and
#the first and last character from a given list 
#of strings.given a list
#['abc','xyz','aba','1221']

def match_words(words):
    ctr=0
    for word in words:
        if len(word)>2 and word[0]==word[-1]:
            ctr+=1
    return ctr
    
print(match_words(['abc','xyz','aba','1221']))

'''write a python program to get a list,sorted in 
increasing order by last element in each tuple from
a given list of non-empty tuples.
sample list:- [(2,5),(1,2),(4,4),(2,3),(2,1)]
expected result:-[(2,1),(1,2),(2,3),(4,4),(2,5)]
'''
def last(n):
    return n[-1]#access last element of tuple

def sort_list_last(tuples):
    result=sorted(tuples,key=last)#sorting according to last element
    return result

print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

#use of sorted function
def sort_list(lst):
    result=sorted(lst)
    return result

print(sort_list([4,6,3,2,1]))

#write a program to remove duplicates from a list
#given list a=[10,20,30,40,50,10,30,90]
'''a=[10,20,30,40,50,10,30,90]
dup_items=set()#set not allow duplicate items
uniq_items=[]
for x in a:
    if x not in uniq_items:
        uniq_items.append(x)
        dup_items.add(x)
print(a)
#o/p:-not correct
'''        
#
lst1=[10,20,30,40,50,10,30,90]
st1=set(lst1)#list converted to set
#since set removes duplicate items, hence list converted to set
print(st1)
lst2=list(st1)#set converted to list
print(lst2)
############

#write python program to clone or copy a list
original_list=[10,20,30,44,4]
new_list=list(original_list)
print("original list:",original_list)
print("new list:",new_list)

#write python program to find the list of words
#that are longer than n from a given list of words

#here n=3 find words longer than 3
def long_words(n,str):
    word_len=[]
    txt=str.split(" ")
    for x in txt:
        if len(x)>n:
            word_len.append(x)
    return word_len
print(long_words(3,"The quick brown fox jumps over the lazy dog"))
    
#write python function that takes two lists and returns
#True if they have as least one common member
def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result = True
                return result
print(common_data([1,2,3,4,5],[5,6,7,8,9] ))
print(common_data([1,2,3,4,5],[6,7,8,9]))

'''
#or for above program
list1=[1,2,4,6,7]
st1=set(list1)
list2=[5,6,8,9,0]
st2=set(list2)
if st1&st2 ==True:
    result=True
    return result
#o/p:not correct
'''
#calculate diff of two lists
#write python program to find unique elements of list1
#list2 and concatenate that elements
list1=[1,3,5,2,7]
list2=[1,2,6,8,3]
diff1=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
total_diff=diff1+diff2
print(total_diff)

#write program to convert list of characters into a string
s=['a','b','c','d','e']
str1=''.join(s)
print(str1) 
#very imp function

#write program to find index of an item in list
num=[10,4,30,-6]
print(num.index(30))  #used for recommendation engine

#write program to append list to second list
list1=[1,2,3,4,5]
list2=['red','Green','Black']
final_list=list1+list2
print(final_list)

