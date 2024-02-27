# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:31:26 2023

"""
#reading line by line
filename='pi_digits.txt'
#we assign the name of file we are reading from to the variable
with open(filename) as file_object:
    #we again use the with syntax to
    #let python open and close
    #the file properly
    for line in file_object:
        print(line)

#the file read line by line the output contains 
#blank line
#these blank lines appear because an invisible newline
#character is at the end of each line in text file

filename='pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
#working with files contain 
#after you have read a file into memory
#you can do whatever you want with that data
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string+=line.strip()
        print(pi_string)
        print(len(pi_string))
        
###################
#one of the simplest ways to save data is to write it
#to a file,when you write text to file
#the output will be still available after 
#you close the terminal containing your program's output.
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")

#########
#writing multiple lines

filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new game.")
    
###########
#to get including new lines by vertical manner
#use \n for new line
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new game.\n")
    
    
#appending file
#when write method used then the previous content
#vanishes and new content is add
#while in append mode the content add to existing file
filename='programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    
################
#