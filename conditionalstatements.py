# if.....else...
# loops
votes = 0
if votes > 10000:
    print(f"You got {votes} and therefore you win!")
else:
    print(f"You got {votes} and therefore you fail!")
# input from user
age = int(input("What is your age? "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not 18+.")

number = int(input("Enter your number:"))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
