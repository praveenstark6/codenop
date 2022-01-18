"""
Getting user input using function
input()

This will be string initially 
to convert it as number or any other data type we want
we can use casting

int(input())
float(input())
bool(input())

like this we can cast the input while getting it.

for getting multiple inputs from same line
we can use split() method of string

names = input().split()

if we give two names, we can write as below

first_name, second_name = input().split()

"""


# Age Calculator
dob = input("enter date of birth(dd/mm/yyyy): ")
birth_year = int(dob[-4:])
current_year = 2022
print("Your age is", current_year - birth_year)



