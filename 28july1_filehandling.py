# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:21:05 2023
"""
'''
I love programming.I love creating new games.I also love finding meaning in large datasets.
I love creating apps that can run in a browser.

3.1415926535
8979323846
2643383279
'''
#file handling 
#file is block of bytes they are arrange in sequentially

#file handling in python

with open('pi_digits.txt') as file_object:
    #pidigits.txt is in harddisk when it called it goes in primary memory
    #the open() function needs
    #one argument: the name of file you want to open
    contents=file_object.read()
print(contents)

#
with open('pi_digits.txt') as file_object:
     contents=file_object.read()
print(contents.rstrip())
#rstrip() method removes,or strips , any white space
#characters from right side of string

########
#two types of path 1.relative path 2.absolute path
#relative path consist only file name
#absolute path has absolute path
#windows cosist / (back slash)
#linux cosist \ (front slash)

file_path='c:/1-Python/pi_digits.txt'
with open('pi_digits.txt') as file_object:
     contents=file_object.read()
print(contents.rstrip())

#in absolute path no need to select directory but in
#relative path need to select directory