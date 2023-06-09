# testing intialising dict with class instances

# in quantconnect they sometimes use class foo(object)
# this was python 2 syntax so its written in the case old code was in python 2 so as to no break it 
# https://stackoverflow.com/questions/332255/difference-between-class-foo-and-class-fooobject-in-python
# https://mail.python.org/pipermail/python-dev/2014-August/135701.html
class SelectionData(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

bill = SelectionData("BILL", 21)
print(bill.__dict__)


class QCAlgorithm:
    def startdate(self, yeardate):
        self.yeardate = yeardate


class EMAMomentumUniverse(QCAlgorithm):
    def Initialize(self):
        self.startdate(1969)
        self.averages = {}
    
    def CoarseSelectionFunction(self, symbol):
        self.averages[symbol] = SelectionData("HULK", 999)
    
will = EMAMomentumUniverse()
will.Initialize()
print(will.__dict__)
will.CoarseSelectionFunction("Marvel")
print(will.__dict__)
# we have not assigned a return value liek we usualy do to the object
# instead we have a dict pointing to the instance of the object
# to access the object just treat it as instance liek below
print(will.averages["Marvel"].__dict__)



