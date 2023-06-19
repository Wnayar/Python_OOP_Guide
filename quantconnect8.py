hero = {"franchise": "marvel", "age": 21, "strong?": True}
print(hero)
# .items() returns a view object. The view object contains the key-value pairs of the dict as tuples in a list
print(hero.items())

for x, y in hero.items():
    print(x, y)

# can only unpack up to as many items per tuple there is
for x, y in hero.items():
    print(x, y)


for x in hero.items():
    print(x)