# Python OOP Tutorial 5: Special (Magic/Dunder) Methods
# https://youtu.be/3ohzBxoFHAY


# DUNDER/MAGIC METHODS, __repr__, __str__, etc


class Employee:

    raise_amt = 1.04
    
    # dunder/magic numbers are the double underscore method __init__ etc, __repr__, __str__
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    # __repr__ is more so for developers, __str__ is more so for user
    # if there is not __str__, when call __str__ it will fall on __repr__
    # good practice is code that cna recreate the object
    # so it changes the return from being the object location at hexidiecimal etc into this format instead
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # if you have the str method the print will default to this one, but u can still call those repr or str functions
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    # left side of addtion is self, right side is the other
    def __add__(self, other):
        return self.pay + other.pay
    
    # just showcasing anogther dunder method __len__
    def __len__(self):
        return len(self.fullname())
    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
# showcasing different ways to call the dunder/magiv methods
print(emp_1.__repr__())
print(repr(emp_1))
print(emp_1.__str__())
print(str(emp_1))

# there are many dunder methods
print(1 + 2)
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

# __add__ method in class
print(emp_1 + emp_2)

# there are many dunder methods for arthmethics just refer to the documentation 
print(len("test"))
# so above is actually just calling a dunder method, because below does the same thing
# so if you think about it the "test", is an instance of the string class and we are callign the inbuilt dunder __len__ method on it 
# that is why if u call len on my employee class it will get an error
print('test'.__len__())

# so if you wanted the len dunder method to work on our object we have to created the len dunder method
print(len(emp_1))

# in documentation you may see if, then later return not implemented, what tshi means if this object doesnt know how to handle it, it wont throw an error it will see if the other object knows how to do it

# also side note string literal vs string object 
# https://stackoverflow.com/questions/61982661/how-can-a-string-object-be-built-from-a-string-literal see answer by DanielB
# x is assigned an integer valye with the literal "5"
x = 5 
print(isinstance(x, int))
# foo is assigned a a str value using the literal "hello"
foo = "hello"
print(isinstance(foo, str))