# arithmetic operators(+.-./.%.*)
from math import remainder

a = 23
c = 14
total = a + c
print("The total is",total)
print(f'The total is {total}')
subtract = a - c
print("The subtract is",subtract)
print(f'The subtract is{subtract}')
remainder = a%c
print("The remainder is",remainder)
print(f'The remainder is{remainder}')
multiplication = a * c
print(f'The multiplication is {multiplication}')
division = a / c
print(f'The division is {division}')
# comparison operators(==,!=,>=,<=,<,>)
age1 = 23
age2 = 12
print(f'Is age1 equal to age2? {age1 == age2}')
print(f'Is age1 greater than age2? {age1 > age2}')
print(f'Is age1 less than age2? {age1 < age2}')
print(f'Is age1 greater than or equal to age2? {age1 >= age2}')
print(f'Is age1 less than or equal to age2? {age1 <= age2}')
print(f'Is age1 not equal to age2? {age1 != age2}')
# logical operators(and,or,not)
math = 67
science = 56
swahili = 78
french = 59
print(math>science and swahili>french)
print(math<science and swahili<french)
print(math>=science and swahili<=french)
print(math>science or swahili>french)
print(math<science or swahili<french)
print(not(math>=science or swahili<=french))

# input from user
first_number = float(input("Enter first number"))
print(f'The first number is {first_number}')
second_number = float(input("Enter second number"))
print(f'The second number is {second_number}')
third_number = float(input("Enter third number"))
print(f'The third number is {third_number}')
fourth_number = float(input("Enter fourth number"))
print(f'The fourth number is {fourth_number}')
division1 = first_number/second_number
print(f'The firts and second division is {division1}')
division2 = third_number/fourth_number
print(f'The third and fourth division is {division2}')
print(f'Is division1 greater than division2 {division1>division2}')
print(f'Is division1 less than division2 {division1<division2}')
print(f'Is division1 equal to division2 {division1==division2}')
print(f'Is division1 greater than or equal to division2 {division1>=division2}')
print(f'Is division1 less than or equal to division2 {division1<=division2}')
print(f'Is division1 not equal to division2 {division1!=division2}')

print(f'The results are positive {division1>0 and division2>0}')
print(f'The results are negative {division1<0 and division2<0}')
print(f'One of the results is zero {division1==0 and division2==0}')

user_name = input("Enter your username")
print(f'The username is {user_name}')
password = input("Enter your password")
print(f'The password is {password}')
print(f'Is username and passwword correct  {user_name=="admin" and password=="secure123"}')
