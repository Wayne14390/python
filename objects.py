from classes import Person, Employee, Rectangle, Car, Emobilis_Employee, Developer, Teacher, Commision_Employee

person1 = Person()
print(person1.first_name)
print(person1.last_name)
print(person1.gender)
print(person1.age)

person2 = Person()
print(person2.first_name)
print(person2.last_name)
print(person2.gender)
print(person2.age)

employee1 = Employee("John","Male",30000,34,"developer")
employee2 = Employee("Ann","Female",20500,18,"nurse")
employee3 = Employee("Peter","Male",10000,23,"security")

print(employee1.basic_salary)
print(employee2.gender)
print(employee3.position)

print(employee1.display())
print(employee2.display())
print(employee3.display())

print(employee1.full_salary())
print(employee2.full_salary())
print(employee3.full_salary())

print(f'new salary for employee 1 : {employee1.new_salary()}')
print(f'new salary for employee 2 : {employee2.new_salary()}')
print(f'new salary for employee 3 : {employee3.new_salary()}')

car1 = Car("USA","Alpha Romeo",1925)
car2 = Car("Germany","Audi",1975)
car3 = Car("Spain","Arizona",1955)

print(f'car model 1 is {car1.model}')
print(f'car model 2 is {car2.model}')
print(f'car model 3 is {car3.model}')

rectangle1 = Rectangle(10,20)
rectangle2 = Rectangle(60,40)
rectangle3 = Rectangle(50,80)

print(f'Area of rectangle1: {rectangle1.area()}')
print(f'Area of rectangle2: {rectangle2.area()}')
print(f'Area of rectangle3: {rectangle3.area()}')

print(f'Perimeter of rectangle1: {rectangle1.perimeter()}')
print(f'Perimeter of rectangle2: {rectangle2.perimeter()}')
print(f'Perimeter of rectangle3: {rectangle3.perimeter()}')

print(f'Measurement of rectangle1: {rectangle1.display()}')
print(f'Measurement of rectangle2: {rectangle2.display()}')
print(f'Measurement of rectangle3: {rectangle3.display()}')

emobilis_employee1 = Emobilis_Employee("Wayne","Male",230000,21,"Degree")
emobilis_employee2 = Emobilis_Employee("Kawira","Female",125000,18,"Diploma")
emobilis_employee3 = Emobilis_Employee("Ann","Female",200000,24,"Masters")
print(emobilis_employee1.qualification)
print(emobilis_employee2.salary)
print(emobilis_employee1.promotion())
print(emobilis_employee2.promotion())
print(emobilis_employee3.promotion())
developer1 = Developer("John","Male",300000,34,"Degree","Fronted Developer","Python")
developer2 = Developer("Ruth","Female",400000,28,"Diploma","Backend Developer","HTML")
print(developer1.specialisation)
print(developer2.prog_language)
teacher1 = Teacher("Felix","Male",70000,32,"Degree","Kenyan","Normal Teacher","Opera")
teacher2 = Teacher("Martha","Female",100000,47,"Masters","Italian","Head Teacher","None")
print(f'Teacher1 name: {teacher1.name},Gender: {teacher1.gender},age: {teacher1.age},salary: {teacher1.salary},nationality: {teacher1.nationality},stream: {teacher1.stream},rank: {teacher1.rank}')
print(f'Teacher2 name: {teacher2.name},Gender: {teacher2.gender},age: {teacher2.age},salary: {teacher2.salary},nationality: {teacher2.nationality},stream: {teacher2.stream},rank: {teacher2.rank}')
commission_employee1 = Commision_Employee("William","Male",60000,23,"Diploma",1000,12)
print(commission_employee1.commission_salary())