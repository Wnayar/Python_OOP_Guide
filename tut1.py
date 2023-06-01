# Python OOP Tutorial 1: Classes and Instances
# https://youtu.be/ZDa-Z5JzLYM


# CLASSES & METHODS

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# # manual assignment of attributes 
# emp_1.first = "corey"
# emp_1.last = "schafer"

# emp_2.boogey = "wooga"
# emp_2.last = "schumba"

# print(emp_1.first)
# print(emp_2.last)

print('{} {}'.format(emp_1.first, emp_1.last))
# the instance is automtaically passed into the method 
# will get this error if no self in method meaning the instance is passed in TypeError: Employee.fullname() takes 0 positional arguments but 1 was given
print(emp_1.fullname())
# in this case the instanc eu pass in urself 
print(Employee.fullname(emp_1))