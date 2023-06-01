class Employee:

    # class variable
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        # these are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

        # everytime create a employee init function called, so increment the class variable
        # notebly we want the class value to be constant and not overwirtten that why not using self here
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        # so techincally inside the instance the raise amount doesnt exist, python first checks the instance if it doesnt exist it will look in the class or inherited 
        # self.pay = int(self.pay * Employee.raise_amount) thus this works also 
        #  it makes sense to keep as self as looks instance first/crerate then look class so can allow subwriting over
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# so techincally inside the instance the raise amount doesnt exist, python first checks the instance if it doesnt exist it will look in the class or inherited 
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(emp_1.__dict__)
# print(Employee.__dict__)

# Employee.raise_amount = 1.05
# this shows if change class class and all instance change, but if change one instance it creates the raise amount attribute in employee 1 thus python looks in instance firts and gets that befor elookign inc lass
emp_1.raise_amount = 1.05
print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)