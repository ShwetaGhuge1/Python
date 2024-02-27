# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:35:46 2023


"""
'''
create a program using maths and fstring &
tell us how many days,weeks & months we have left 
if we will live until 80 years
'''
#one year contains 365 days
#one year contains 12 months
#one year contains 52 weeks
current_age=int(input("enter your current age:"))
age=int(input("enter your age upto which you live:"))

remaining_year=age-current_age
days=remaining_year*365
month=remaining_year*12
week=remaining_year*52
print(f"remaining days are {days}")#use of fstring
print("remaining months are:",month)
print("remaining years are:",remaining_year)
print("remaining weeks are:",week)
#########
#OR
print("what is your todays age")
years_today=input("years:")
months_today=input("months:")
days_today=input("days:")
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"your total age today in days{total_days_today}")
print("let us assume you are expected to live 90 years")
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"your remaining life in days is {remaining_days_to_live}")


##################
#program for roller coaster
height=int(input("enter your height:"))
age=int(input("enter your age:"))
if height==120 or height>120:
    if(age<18):
        print("ticket will be Rs.20")
    elif(age>18 or age==18):
        print("ticket will be Rs.50")
    elif(age<12 and height==120):
        print("ticket will be Rs.10")
    elif(age>12 and age<18 and height==120):
        print("ticket will be Rs.15")
else:
    print("you are not eligible")

#oR

print("welcome to the roller coaster")
height=int(input("enter your height in cm:"))
bill=0
if height>=120:
    print("you are eligible for roller coaster")
    age=int(input("please enter your age:"))
    if age<12:
        print("child ticket will be $5")
        bill=5
    elif age<=18:
        print("youth tickets are $7")
        bill=7
    else:
        print("adults ticket are $12")
        bill=12
    want_photo=input("do you want photo y or n:")
    if want_photo=='y':
        bill+=3
        print(f"your total bill will be {bill}")
    else:
        print(f"your total bill {bill}")
print("you need to grow your height")

############
