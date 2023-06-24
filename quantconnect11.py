# The following issues explored stemmed from quantconnect forex bootcamp


# SECTION A: ENUMURATE function and Enum class

templist = ["thor", "hulk", "spiderman"]
enumtemplist = enumerate(templist)
print(enumtemplist)
print(type(enumtemplist))
print(list(enumtemplist))

# if did not unpack it produces tuples with index and variable
for x in enumerate(templist):
    print(x)

# can unpack it
for x, y in enumerate(templist):
    print(x, y)

# below explores the enum class, but personally I do not see much value in it on surface level as enumrate function seems to satisfy more issues, however quantconnect api in forex bootcamp mentions it so good to know
# did not have to install enum with pip, it was in python standard library 
# https://peps.python.org/pep-0435/ , read documentation for all other functionaltiies
from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3
    # cant have enum with two same keys, but same values is fine
    # blue = 4
    orange = 2

print(Color.red)
print(Color["red"])
print(Color.red.name)
print(Color(2))
print(repr(Color.red))
print(type(Color.red))
print(isinstance(Color.green, Color))

for color in Color:
    print(color)




# SECTION B: datetime module
# https://www.quantconnect.com/forum/discussion/2786/how-to-use-the-time-object-in-python/p1
# In quantocnnetc time object are from the datetime  module


from datetime import *
print(date.today())
print(date.today().day)
print(date.today().year)

tempdate = date(2000, 1, 28)
print(tempdate)
print(tempdate.today())
print(tempdate.day)




# SECTION C: Round function
x = 5/2
# round function rounds down, which is why its used in the forex bootcamp in calculating the lots, as the broker automitcally rounds down for invalid sizing of order
print(round(x))