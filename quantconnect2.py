# this shows that if return multiple boolean, it only returns true if all true, if one false it returns false, which makes sense true and false means false
# it is esentially evaluating the statement


def test():
    return True and False

def test1():
    return True and True

def test2():
    return False and True

def test3():
    return False and False

def test4():
    return True and True and False

def test5():
    return True and True and True

# as you can see this evalautes to true as expected because for or just need oen to be true to evalaute to true 
def newtest():
    return True or False or True or False or False

# basically if want to return multiple values use comma, seems to default to a tuple
def returnmultiple():
    return True, False

print(test())
print(test1())
print(test2())
print(test3())
print(test4())
print(test5())
print(newtest())
print(type(returnmultiple()), returnmultiple())
