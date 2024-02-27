# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:12:42 2023

@author: rohit
"""
'''UTF - Unicode Transformation format
 and In UTF-8, '8' means 8-bit values are used in the 
 encoding. It is one of the most efficient and convinient 
 encoding formats among various encodings.

'''
string1="apple"
string2="jeet125"
string3="12345"
string4="pre@12"

string1.encode(encoding='UTF-8',errors='strict')
string2.encode(encoding='UTF-8',errors='strict')
string3.encode(encoding='UTF-8',errors='strict')
string4.encode(encoding='UTF-8',errors='strict')
#not get as it is o/p

###########################################

text="one 🐘 and three 🐋"
print(text)
print(len(text))

'''
we encode the string into a byte type using the
utf8 encoding and print the bytes.
we count the number of bytes in this encoding type.
'''

e=text.encode('utf8')
print(e)
print(len(e))

#############################################
fname='data.txt'

with open(fname,mode='rb') as f:
    #by default it encodes in utf-8
    contents=f.read()
    
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))
    
####################################
#for utf-16
fname='data.txt'

with open(fname,mode='rb') as f:#'rb' for reading pattern
    #by default it encodes in utf-8
    contents=f.read()
    
    print(type(contents))
    print(contents)
    print(contents.decode('utf16'))
    
#o/p:- get the error 
#########################################

#NFC and NFD:- 
'''
normalization form d is called NFD
and 
Normalization form c is called NFC
There is no diff between NFC and NFD
both are normalization technique 
intended for creating/generating code 
compatible to the platform
'''
#Normalizing Unicode

s1='Spicy Jalope\u00f1o'
s2='Spicy Jalopen\u0303o'
print(s1)
print(s2)
s1==s2

import unicodedata
t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
t1==t2
#True
print(ascii(t1))

#############################################
 
#stripping
#Unwanted characters from strings

#whitespace stripping
s='   hello world   \n'
s.strip()

#hello world
s='   hello world    \n'
s.lstrip()

#'hello world \n'
s.rstrip()
s='    hello world   \n'
#' hello world' 

#character stripping
t='-----hello-----'
t.lstrip('-')
#'hello===='
t.strip('-=')
#'hello'

t='-----hello====='
t.lstrip('-')
#'hello===='
t.strip('-=')
#'hello'


s=' hello world   \n'
s=s.strip()
s
#'hello world'

s.replace(' ','')
#'helloworld' 

import re
re.sub('\s+','',s)
"hello world"

import re
re.sub('\s+',' ',s)
"hello world"

#aligning the text
text='Hello World'
text.ljust(20)
#'Hello World   '
text.rjust(20)
#'     Hello World'
text.center(20)
#'    Hello World     '

########################################
#all of these methods accept an optional 
text.rjust(20,'=')
#'=========Hello World'
text.center(20,'*')
#'****Hello World*****'

###################################
format(text,'>20')
#'         Hello World'
format(text,'<20')
#'Hello World         '
format(text,'^20')#^20 means at center
#'    Hello World     '

#here you can add characters to fill the space ...
#as above but if you want to include..
#####################################
#
format(text,'=>20s')
#'=========Hello World'
format(text,'*^20s')
#'****Hello World*****'

#these format codes can also be used in format()

'{:>10s} {:>10s}'.format('Hello','World')
#'     Hello      World'


######################
x=1.2345
format(x,'>10')
x
#'    1.2345'

format(x,'>10.2f')
#'      1.23'
################
#ready ref page
parts=['Is','Chicago','Not','Chicago?']
' '.join(parts)
'Is Chicago Not Chicago?'
','.join(parts)
'Is,Chicago,Not,Chicago?'
''.join(parts)
'IsChicagoNotChicago'
