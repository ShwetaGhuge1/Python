# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 08:43:18 2023

@author: rohit
"""
#use of elif statement

savings=float(input("enter how much savings"))
if savings==0:
    print("Sorry no saving")
elif savings<500:
    print("well done")
elif savings<1000:
    print("thats a tidy sum")
elif savings<10000:
    print("Welcome sir")
else:
    print("thank you")

#looping
#while loop
'''
is used to iterative
it is used as long as the condition is true
'''
count=1
print('starting')
while count <=10:
    print(count)
    count+=1
    
#for loop
#loop over a set of values in a range
print("print out values in a range")
for i in range(2,10):
    #print from 2 to 9
    print(i)
    print("Done")
    
###########
#this code uses for loop,if,break statement
    
print("only print code if all iterations completed")
num=int(input("enter a number to check for"))
for i in range(0,16):
    if(i==num):
        break
    print(i)
print("Done")

##############
#now use an 'anonymous' loop variable
#anonymous variable is _
#without using i,j,k variables
for _ in range(0,10):
    print('.',end='')
    print()
    
##
for _ in range(0,10):
    print('.',end='')

#################################
#Break loop statement
#location of print statement
num=int(input("enter number"))
for i in range(0,6):
    if i==num:
        break
    print(i,'',end='')
print('Done')
##location of print statement is changed
num=int(input("enter number"))
for i in range(0,6):
    if i==num:
        break
    print(i,'',end='')
    print('Done')
#######################
#python code to print odd numbers
##x,y=4,19 means x=4 and y=19 another method 
#of declaration of variable
#it is important question for interview
#to print even and odd numbers
start,end=4,19
#iterating each number in list
for num in range(start,end+1):
    #checking condition
    if num%2!=0:
        print(num,end=" ")

#################
#to print even numbers
start,end=4,19
#iterating each number in list
for num in range(start,end+1):
    #checking condition
    if num%2==0:
        print(num,end=" ")
        print()
        
#################
#python program for even numbers in range
for even_numbers in range(4,15,2):
    #here inside range first number is starting
    #second end
    #third is interval
    print(even_numbers,end=' ')
    
#python program for odd numbers in range
for odd_numbers in range(3,16,2):
    print(odd_numbers,end=' ')
    
#even numbers tking range from user
start=int(input("enter the starting of range"))
end=int(input("enter the ending of range"))
for num in range(start,end+1):
    if num%2==0:
        print(num,end=' ')
        
#odd numbers tking range from user
start=int(input("enter the starting of range"))
end=int(input("enter the ending of range"))
for num in range(start,end+1):
    if num%2!=0:
        print(num,end=' ')
    

###########
#to print prime number
start=int(input("enter starting number"))
end=int(input("enter ending number"))
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')
        
###OR

######
###prime number
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "the number is not prime"
            break
    return "the number is prime"
prime_num(17)
                
###############
#to print leap year
year=int(input("enter the year:"))
if year%4==0 or year%400==0 and year%100!=0:
    print("this is leap year")
else:
    print("this is not leap year")
    
#OR

##leap year code
def is_leap_year(year):
    if((year>0) and (year%4==0)and(year%100==0)and(year%400==0)):
        return True
    return False

print(is_leap_year(1900))

##
    
######################
#check given string is palindrome or not

str1=input("enter the string:")
if(str1==str1[::-1]):
    print("the string is palindrome")
else:
    print("not palindrome")
'''rev=""
x=str1
while i>0:
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print("palindrome")
else:
    print("not palindrome")
   ''' 