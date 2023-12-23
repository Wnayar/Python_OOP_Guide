# an attempt to understand how quantconnect works refer to the video link for the code that sparked this .py file link @3.25: https://youtu.be/WQwyKfef80k
# no boogey
class Person:

    def __init__(self, name):
        self.name = name


    def intialize(self, age):
        self.age = age
    

    def setstartdate(self, date):
        self.date = date


    def addequity(self, equity):
        self.equity = equity
        return "boogey"


bill = Person("BILL")
print(bill.__dict__)
bill.intialize(2)
print(bill.__dict__)
bill.intialize(3)
print(bill.__dict__)
bill.setstartdate(2099)
print(bill.__dict__)


class orangefish(Person):

    # overwrite intialize
    def intialize(self, age):
        self.age = age * 2
        # so quant connect is just tryign to set up everything at once, its doen this way as of course dotn want to ask for user input on the command line nor have to write code to intliaze it outside the class
        # so this is the way they are doing it , im just calling a function to set up the date attribute
        self.setstartdate(2023)
        # trying to intalize on the set up, coudl set up date like this also without using a function 
        self.testnumber = 4
        testvariable = self.addequity("SPY")
        self.testvariable = testvariable


will = orangefish("Will")
will.intialize(6)
print(will.__dict__)
print(will.date)
print(will.testvariable)


