class Employee:
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.set_salary(salary)

    def set_salary(self, salary):
        if salary > 0:
            self.salary = salary
        else:
            raise ValueError("Salary must be greater than zero.")

try:
    emp1 = Employee("John Doe", 30, "Male", 50000)
    print(f"Employee 1: {emp1.name}, {emp1.age} years old, {emp1.gender}, Salary: {emp1.salary}")
except ValueError as e:
    print(e)

try:
    emp2 = Employee("Jane Doe", 25, "Female", -10000)
    print(f"Employee 2: {emp2.name}, {emp2.age} years old, {emp2.gender}, Salary: {emp2.salary}")
except ValueError as e:
    print(e)