class Person:
    first_name = "Alex"
    last_name = "Kibunja"
    gender = "Male"
    age = 18

class Employee:
    def __init__(self, name, gender, basic_salary, age, position):
        self.name = name
        self.gender = gender
        self.basic_salary = basic_salary
        self.age = age
        self.position = position

    def display(self):
            return f"Name: {self.name}, Gender: {self.gender} "
    def full_salary(self):
        full_salary = self.basic_salary + 25000
        return full_salary
    def new_salary(self):
        new_salary = self.basic_salary + (0.27 * self.basic_salary)
        return new_salary

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def display(self):
        return f"Width: {self.width}, Height: {self.height} "

class Emobilis_Employee:
    def __init__(self, name, gender, salary, age, qualification):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.age = age
        self.qualification = qualification

    def promotion(self):
        if self.qualification == "Degree" or self.qualification == "Masters":
            return "You are promoted"
        else:
            return "You are not promoted"

class Developer(Emobilis_Employee):
    def __init__(self, name, gender, salary, age, qualification,specialisation, prog_language):
        super().__init__(nder, salary, age, qualification)
        self.specialisation = specialisation
        self.prog_language = prog_language
class Teacher(Emobilis_Employee):
    def __init__(self, name, gender, salary, age, qualification,nationality,rank,stream):
        name, gesuper().__init__(name, gender, salary, age, qualification)
        self.nationality = nationality
        self.rank = rank
        self.stream = stream

class Commision_Employee(Emobilis_Employee):
    def __init__(self, name, gender, salary, age, qualification, commission_rate,hours_worked,):
        super().__init__(name, gender, salary, age, qualification)
        self.commission_rate = commission_rate
        self.hours_worked = hours_worked

    def commission_salary(self):
        commission_salary = (self.commission_rate * self.hours_worked) + self.salary
        return commission_salary

