# create a class with class and instance variables
# utilise dict method to see 

class Person:

    grow_up = 2
    name_sample = "Spiderman"

    def __init__(self, age, name, occupation):
        self.age = age
        self.name = name
        self.occupation = occupation 
    
    # by putting self can allow overwrite of class variable 
    def grown(self):
        # self.age += Person.grow_up   , in this case cant overwrite
        self.age += self.grow_up

    # this is an exmaple where cant overwitre because put class variable
    def become_spiderman(self):
        self.name = Person.name_sample

bill = Person(21, "BILL", "Quant")

print(bill.age)
print(bill.__dict__)

bill.grown()
print(bill.__dict__)

# here we overwrite by creating within the instance a variable with the same name as the class variable
#  python will look at the instance for highest piority than the class after if that variabel not in inside which is why this works
bill.grow_up = 90
print(bill.__dict__)

bill.grown()
print(bill.__dict__)

bill.become_spiderman()
print(bill.__dict__)

# so even thou we change the below name_sample because we put Person the class above it takes that 
bill.name_sample = "NotSpiderman"
print(bill.__dict__)

bill.become_spiderman()
print(bill.__dict__)