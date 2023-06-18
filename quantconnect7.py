# Exploring basic python functionality used in quantconnect lesson 11 tiingo alternative data

# sum on list
testlist = [1, 2, 5]
print(sum(testlist))

# pop() function python
 
# pop() on list where the input is the index 
# it returns the variable at that index in the list
x = testlist.pop(2)
print(testlist)
print(x)

# pop() on dict
testdict = {"age": 21, "type": "superhero", "franchise": "marvel"}
print(testdict)
# to pop have to access by key, it will return the value deleted
y = testdict.pop("age")
print(testdict)
print(y)
#optional can add aditional paramater to pop for the default return value if key does not exists, this is done to prevent an error being thrown 
z = testdict.pop("random", None)

