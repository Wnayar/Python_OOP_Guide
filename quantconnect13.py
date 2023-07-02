# testing logic flow and inaction of if elif else statements used in conjunction
# refer to https://youtu.be/_BHi5Y2Aow4  , Algorithmic Trading Using Python #6 - Indicators & Historical Data

x = 5


#  so this is the logic used in quantconnect, essentially even if it passes the first if, if it fails the nested if it will just ingore all the othet elif and else which is why they opt to use this structure instead of just if statements
if x > 3:
    if x > 5:
        print("foo")
elif x > 4:
    print("bar")
else:
    print("baz")