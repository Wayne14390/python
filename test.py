# # input from user
# secret_code = float(input("Enter the secret code: "))
# print(f"The secret code is {secret_code>50 and secret_code<100}")
# # dictionary
# book = {
#     'title' : 'Samaritan',
#     'author' : 'Wayne',
#      'publisher' : 'klb',
#      'key' : '1232'
# }
# print(book)
#
# if 'key' in book:
#     print('key is present')
# else :
#     print('key is not present')
age = int(input("Enter your age: "))
print(age)
if age > 0 and age <= 2:
    print('You are a baby.')
elif age > 2 and age <= 4:
    print('You are a toddler.')
elif age > 4 and age <= 13 :
    print('You are a child.')
elif age > 13 and age <= 20 :
    print('You are a teenager.')
elif age > 20 and age <= 35 :
    print('You are a young adult.')
elif age > 35 and age <= 60 :
    print('You are a middle-aged adult.')
else:
    print('You are a senior citizen.')
print('Age is just a number, enjoy life!')

current_temperature = float(input("Enter your current temperature: "))
print(f'{current_temperature} degrees celsius')
if current_temperature > 30:
    print('Its a hot day.')
elif current_temperature <= 30 and current_temperature > 20:
    print('Its a warm day.')
else:
    print('Its a cold day.')

withdrawal_amount = float(input("Enter your withdrawal amount: "))
if withdrawal_amount > 10000:
    withdrawal_amount = withdrawal_amount + (withdrawal_amount *0.1)
    print(f'Withdrawal amount: {withdrawal_amount}.')
elif withdrawal_amount > 5000:
    withdrawal_amount = withdrawal_amount + (withdrawal_amount *0.05)
    print(f'Withdrawal amount: {withdrawal_amount}.')
else:
    print(f'Withdrawal amount: {withdrawal_amount}.')


