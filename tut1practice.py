# create a class with attributes defined when u make it
# create a method within that class 

class Person:

    def __init__(self, race, age, occupation):
        self.race = race
        self.age = age
        self.occupation = occupation



    def status(self):
        return '{}, {}, {}'.format(self.age, self.race, self.occupation)
    
bill = Person('Chinese', 21, 'Quant')

print(bill.age)
print(bill.status())

bill.test = 'weird'
print(bill.test)
