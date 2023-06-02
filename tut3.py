# Python OOP Tutorial 3: classmethods and staticmethods
# https://youtu.be/rq8cL2XMM5M


# REGULAR METHODS(self instance) VS CLASS METHODS(class) VS STATIC METHODS(neither of the previous two)


import datetime

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1
    
    # this is a regular method it takes the instance as the first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    # this is a class method, recieve class as first instance instead of self, cls is just convention name cant sue class as that is a keyword
    #  so here we are working with the class instead of the instance 
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        # was just testign to create on the go a class variable
        # cls.test = amount
    
    # using class method as an alternate constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # Employee(first, last, pay) is same thing but cls is just easier to type
        #  need to put return so they can assign the employee object to something
        return cls(first, last, pay)

    # regular methods take in self instance, class method takes in class, but static methods dont take either of these
    # static method are kind of just like normal functions but put into a class because they are kind of linked
    # if nto using self or class, prob nmeans hsould be a static
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday() == 6:
            return False
        return True

my_date = datetime.date(2016, 11, 10)
print(Employee.is_workday(my_date))

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

# so this way dotn need to parse string anymore manually can just call class method because common use case 
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# so we run the class method, we are workign with the class variable
# Employee.set_raise_amt(1.05)
# can also run the class method from the instance will create in class not instance but doesnt rly make sense to do so 
# emp_1.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_1.raise_amt)
# print(Employee.__dict__) 
# print(emp_1.__dict__)