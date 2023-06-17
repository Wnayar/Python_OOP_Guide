# create a class with getter (@property), setter and deleter methods
# test the functionality

class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # using getter, @property, so dont need to put brackets, use case is usualy to not break code when making changes, and to allow the use of setter and deleter method which require getter @ property to be set up
    @property
    def growup(self):
        self.age = self.age + 100
    
    # setter function (requires getter function @property to be set up)
    # note it has to be same name of the function u want to put a setter on 
    # note setter function only allowed to take in one input, so if want more liek this case use a tuple or list
    @growup.setter
    def growup(self, greatname_wiseupage_tuple):
        self.name = greatname_wiseupage_tuple[0]
        self.age = greatname_wiseupage_tuple[1]

    # deleter function (requires getter function @property to be set up)
    @growup.deleter
    def growup(self):
        print("Deleted the variables held within the instance, but the instance exists still")
        self.name = None
        self.age = None

bill = Human("Bill", 21)
print(bill.__dict__)

# using getter, @property, so dont need to put brackets, use case is usualy to not break code when making changes, and to allow the use of setter and deleter method which require getter @ property to be set up 
bill.growup
print(bill.__dict__)

# note setter function only allowed to take in one input, so if want more liek this case use a tuple or list
bill.growup = ("KINGBILL", 999)
print(bill.__dict__)

# so this says we want to calls the deleter function inside our instance linked to that function 
# in this example we are setting all the variables to none, but not the oobject instance still exists
del bill.growup
print(bill)
print(bill.__dict__)

# this line below will delete the instance 
del bill
