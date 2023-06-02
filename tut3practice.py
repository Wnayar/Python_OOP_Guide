# create a regular method, class method, static method within a class
# test out its functionality 

class Person:

    payincrease = 1.10

    def __init__(self, name, age, occupation, pay):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.pay = pay 

    # regular method (instance, passing in self)
    def becomehulk(self):
        self.name = "Hulk"
    
    # regular method to update pay
    def updatepay(self):
        # to call class variable need to to do class.
        self.pay = self.pay * Person.payincrease

    # class method (passing in class)
    @classmethod
    def huge_pay_increase(cls, payincrement):
        cls.payincrease = payincrement
        return print("Everyone's pay has been increased to a {} multiple of original amount".format(cls.payincrease))
    
    # static method (not passign in self or class, kind of just thrown into a class because kind of linked)
    @staticmethod
    def summon_a_hero(nameofhero):
        print("{} has been summoned, RUN!!!".format(nameofhero))


bill = Person("BILL", 21, "Quant", 100000)
bill.becomehulk()
print(bill.__dict__)

Person.huge_pay_increase(1.50)
print(Person.__dict__)

bill.updatepay()
print(bill.__dict__)

# typically calling static method through the class as that is where it resides 
Person.summon_a_hero("THOR")