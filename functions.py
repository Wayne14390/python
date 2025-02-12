def my_function():
    print("Hello world")

my_function()
my_function()
my_function()

def my_function2():
    salute = "Hello world"
    print(salute)

my_function2()

def customers(salute):
    print(salute)
customers("Hello world")
customers("Hello James")
customers("Hello Ann")

def employees(first_name, last_name, age):
    print(f'Hello {first_name} {last_name} {age}')

employees("Hillary","Kiptoo",17)
employees("Esther","Munene",12)
employees("William","Castro",34 )

def numbers(first_number, second_number):
    summation = first_number + second_number
    subtraction = first_number - second_number
    return (f'The summation is of {first_number} and {second_number} is: {summation}, the subtraction is: {subtraction}')

arithmetic = numbers(10, 20)
print(arithmetic)

def age_calculator(current_age):
    new_age = current_age + 36
    return new_age

age_calculator(17)
print(f'Your age in the next 36 years will be   {age_calculator(17)}')

def bet_bonus(name,correct_score):
     if correct_score >= 9 and correct_score <= 13:
         return f'{name} bonus is 5000'
     elif correct_score >= 6 and correct_score <= 9:
         return f'{name} bonus is 9000'
     elif correct_score >= 4 and correct_score <= 6:
         return f'{name} bonus is 2000'
     else:
         return f'{name} bonus is 0'

print(bet_bonus("Paul",8))
print(bet_bonus("Nyamu",13))
print(bet_bonus("Wayne",2))


def greet (name):
    if name == "Alice" or name == "Bob":
        return f'Hello, {name}'
    else:
        return "Hello"

print(greet("Alice"))
print(greet("Bob"))
print(greet("Wayne"))
