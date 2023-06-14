# create 2 sub classes of a main class one identical, one which modifies init, modifies class variables, modiefies class methods, add class methods
# test out using print(help(<whicever class>)) to see method resolution order
# test out using print isinstance(a, b) and issubclass(a, b) where checking if a is an insatnce or b in the former, or if a is a subclass of b in the latter

class Person:

    payraise = 1.10

    def __init__(self, name, age, occupation, pay):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.pay = pay 

    # regular method, self instance
    def become_hulk(self):
        self.name = "HULK"
    
    def increase_pay(self):
        # note here even thou self.payraise doesnt exist, python will look one level higher up in the class to find it unless overwrite it manually
        self.pay = self.pay * self.payraise
    
    #  class method, class
    @classmethod
    def change_pay_raise(cls, newpayraise):
        Person.payraise = newpayraise
    
    # static method, neither of the above
    @staticmethod
    def summon_hero(heroname):
        print("{} is summoned, RUN!!!!!!".format(heroname))


class Personcopy(Person):
    pass

class Elites(Person):

    # overwtining Person class varaible
    payraise = 1.5

    def __init__(self, name, age, occupation, pay, royalfamily):
        Person.__init__(self, name, age, occupation, pay)
        # super is another way to do but same outcome, super doesnt need self
        # for super we pass in those arguments into our parent class which takes care of it for us, then we just have to worry about the addiotnal stuff
        # super().__init__(name, age, occupation, pay)
        self.royalfamily = royalfamily 
    
    # overwrting Person become hulk function
    def become_hulk(self):
        self.name = "THE ROYAL HULK"

Will = Personcopy("WILL", 21, "QuantChad", 5000000)
Bill = Elites("BILL", 21, "Quant", 1000000, "KING")
print(Will.__dict__)
print(Bill.__dict__)

Bill.increase_pay()
print(Bill.__dict__)
Bill.become_hulk()
print(Bill.__dict__)

# shows method resolution order and other useful info, press q to quit terminal 
# print(help(Elites))

# using isinstance and issubclass 
print(isinstance(Bill, Elites))
print(isinstance(Bill, Person))
print(isinstance(Bill, Personcopy))
print()
print(issubclass(Elites, Elites))
print(issubclass(Elites, Person))
print(issubclass(Elites, Personcopy))