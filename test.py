# input from user
secret_code = float(input("Enter the secret code: "))
print(f"The secret code is {secret_code>50 and secret_code<100}")
# dictionary
book = {
    'title' : 'Samaritan',
    'author' : 'Wayne',
     'publisher' : 'klb',
     'key' : '1232'
}
print(book)

if 'key' in book:
    print('key is present')
else :
    print('key is not present')
