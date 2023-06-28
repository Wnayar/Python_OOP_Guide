from datetime import datetime, timedelta
# so here datetime and timedelta are objects within the datetime module
# just bad naming convention imo to have a class the same name as the module i.e datetime
x = datetime.min
y = datetime.hour
z = datetime.now()

print(x)
print(y)
print(z)

print(timedelta(31))
print(datetime.now() + timedelta(31))




# just exploring A importing everything
# from datetime import *
# x = datetime.min
# y = datetime.hour
# z = datetime.now()

# print(x)
# print(y)
# print(z)

# print(timedelta(31))
# print(datetime.now() + timedelta(31))






# exploring B just import the module, so have to call the module in the code
# import datetime
# x = datetime.datetime.min
# y = datetime.datetime.hour
# z = datetime.datetime.now()

# print(x)
# print(y)
# print(z)

# print(datetime.timedelta(31))
# print(datetime.datetime.now() + datetime.timedelta(31))




# Random testing of list comprehension
templist = [1, 2, 3, 4, 5, 6, 7, 8, True, False, "Foo"]
y = []

for x in templist:
    if isinstance(x, int) and  x > 5:
        y.append(x)

print(y)


z = [x for x in templist if isinstance(x, int) and x > 5]
print(z)


k = [x for x in templist if type(x) == int and x > 5]
print(z)