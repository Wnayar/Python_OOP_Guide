# Python OOP Tutorial 4: Inheritance - Creating Subclasses
# https://youtu.be/RSl87lqOXDE


# INHERITANCE CREATING SUBCLASSES( also with additonal or modiified arguments and methods)


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# instead of copy and pasting, if a lot of shared things between classes can just inherit it instead
# this () allows to inherit from employee class
class Developer(Employee):
    # follows method resolution order which si why 1.1 takes piority here
    raise_amt = 1.10

    # you shoudltn copy and paste all the code from above so instead we do this Employee init handles first few arguments we handle rest 
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # both work the one above or the one below in asking the parent class to handle some of it
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    # can pass in list of employees deafault is none, as he ditn want to pass in mutable items
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())



# first looks in developer class if cant find looks in chain of inheritence, inhertience reolsution order, thus finds it in Employee class
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# passign in dev1 in list format, dev_1 is employee instance
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# great way to see method resolution order, and other userful info 
# print(help(Developer))


# isinstance and issubclass is used to check relationship 
print(isinstance(mgr_1, Manager))
# even a subclass that inhereits is still considered an instance of the parent, and an insatnce of itself
print(isinstance(mgr_1, Employee))
# even thou mananger and developer inherit from employee they are nto part of the same inheretience tree thus not an instance of each other
print(isinstance(mgr_1, Developer))
print()

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
# even thou manager and developer inhereit from employee they are nto subclasses of each other
print(issubclass(Manager, Developer))