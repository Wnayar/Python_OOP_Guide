# this shows that if return multiple boolean, it only returns true if all true, if one false it returns false, which makes sense true and false means false

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


print(test())
print(test1())
print(test2())
print(test3())
print(test4())
print(test5())
