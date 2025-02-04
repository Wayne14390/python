from _pydatetime import date
from datetime import datetime
from functools import total_ordering
from time import strftime

print("Hello World")
print("Hello World")
print("Hello World")
print(12412)
print(132.45)
print("Wayne")

# variables
first_name = "Wayne"
print(first_name)

age = 24
print(age)

weight =60.45
print(weight)

# data types
# integer
a = 654
print(a)
# string
b = "Click to save the form"
print(b)
# float
e = 12322.1235
# boolean
is_on = True
print(is_on)
is_on = False
print(is_on)

# input from user
name = input("What is your name?")
print(name)

age = int(input("How old are you?"))
year_of_birth = date.today().year - age
year_of_turning_100 = year_of_birth + 100

print(" year of turning 100 is",year_of_turning_100)

weight = float(input("How much do you weigh?"))
height = float(input("What is your height?"))
BMI = weight / (height * height)
print(BMI)

# first_number= float(input("input maths marks?"))
# second_number = float(input("input cre marks?"))
# total = first_number + second_number
# print(total)






