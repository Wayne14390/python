# if.....else...
# loops
votes = 10000
if votes > 10000:
    print(f"You got {votes} and therefore you win!")
else:
    print(f"You got {votes} and therefore you fail!")
# input from user
# age = int(input("What is your age? "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not 18+.")
#
# number = int(input("Enter your number:"))
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

marks = 100
if marks > 80 and marks <= 100:
    print(f"You got {marks} and  you have grade A")
elif marks > 70 and marks <= 80:
    print(f"You got {marks} and  you have grade B")
elif marks > 60 and marks <= 70:
    print(f"You got {marks} and  you have grade C")
elif marks > 40 and marks <= 60:
    print(f"You got {marks} and  you have grade D")
elif marks <40 and marks >= 0:
    print(f"You got {marks} and  you have grade E")
else:
    print('Please enter a number between 0 and 100')

