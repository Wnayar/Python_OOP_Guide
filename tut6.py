# Python OOP Tutorial 6: Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters
# https://youtu.be/jCzT9XFZ5bw

class Employee:

    # important to note the init is made on construction meaning if later i go and change self.first the email will still have the original version
    def __init__(self, first, last):
        self.first = first
        self.last = last 
        # self.email = first + '.' + last + '@email.com'
    
    # so problem is self.email will be the old name on change, so a solution coudl be using a method
    # def email(self):
    #     return '{}.{}@email.com'.format(self.first, self.last)
    
    # so the better solution is to use a property decorator 
    # getter function
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    # getter function
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # setter function
    @fullname.setter
    def fullname(self, name):
        # splitting on the space, first name is one on the left, last name is one on the right after the space
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    # deleter function 
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

# emp_1.first = "Jim"

# using the setter
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
# so while factoring out the email to a function instead of under the constructor seems to work
#  the issue is any old code which uses .email will break as now need to add ()
# print(emp_1.email())

# so here we are able to access the method as if it were an attribute, so we dont break old code
print(emp_1.email)

print(emp_1.fullname)

#using the deleter
del emp_1.fullname
print(emp_1.fullname)
print(emp_1.__dict__)




