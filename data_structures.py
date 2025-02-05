# list
employees = ['John', 'Smith', 'Andrew', 'Jane']
print(employees)
print(employees[2])
print(employees[1:3])
employees[3] = 'Reuben'
print(employees)
employees.append('Stephen')
print(employees)
employees.insert(1, 'Julianna')
print(employees)
employees.extend(['Paul', 'Erick', 'Allan'])
print(employees)
# tuple
products = ('apple', 'banana','cherry' ,'orange')
print(products)
print(products[2])
print(products[1:3])
# products[0] = 'Mango'
# set
students = {'Peter', 'Esther', 'Ann', 'Oduor'}
students.add('Dennis')
print(students)
students.update(['Kimani'])
print(students)
students.remove('Ann')
print(students)
# dictionary
book = {
    'title': 'Book title',
    'author': 'Ali',
    'publisher': 'Philadelphia',
}
print(book)
book['year published'] = 2006
print(book)
print(book['author'])
print(book['title'])

if 'author' in book:
    print('Author is in book')
else:
    print('Author is not present')
