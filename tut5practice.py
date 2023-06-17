# create a class with __repr__, __str__, and another dunder method if your choice
# test the functionality of these dunder method and call them in the 2 different ways which produce the same outcome etc, str() or instance.__str__()
 
class Human:

    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    # good practice to format it such that it can be replicated in code when copy and past to make the object
    # repr is more so for developers so that why the code is made to be abel to copy and paste as best practice
    def __repr__(self):
        return "Human({}, '{}')".format(self.age, self.name)
    
    # __str__ is made mroe so for the user interface, so you can put what format you want the user to see slight diff from above which is wantign it to be able to reproduce the code as this is diff target audience
    def __str__(self):
        return "You called the instance of the Human object with the name {}".format(self.name)
    
    # __add__ dunded/magic method
    def __add__(self, other):
        return self.name + ' ' + other.name


bill = Human(21, "Bill")
will = Human(20, "Will")
print(bill)
print(repr(bill))
# when use print, it will deafult to str if have the method, if not will default to repr, can still call these methods individually 
print(str(bill))

# here below is just different ways to call the same dunder methods
print(repr(bill))
print(bill.__repr__())

print(str(bill))
print(bill.__str__())
# and pritn auto defaults to __str__ method if have it, instead of object at 0x... hexidecimal takes away anonymity for end user
print(bill)

# exploring other dunder methods there are many such as __add__
print(1 + 2)
print(int.__add__(1, 2))
print(will + bill)