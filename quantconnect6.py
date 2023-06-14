# Trying to understand the algorithm argument, from what I know if quant connect sets up the function with the argument function it automatucally takes ur instance algorithm
#  that is the algro with the weird name, but if u make ur own function u need to mnaually pass in self, from ur algo to the function as seen below
#  @10:39 min https://youtu.be/yuZBBX47xK0
#  the reason why you would want to pass in your algorithm as an arguement is that u can acccess all the values u have in ur algorithm and also all the helper functions withign the QCalgortihm class which your function inherits from

class QCAlgorithm:
    pass

class Myalgo_weirdname(QCAlgorithm):
    def intialize(self):
        self.returns = 10
        self.universe =  ['BTCUSD', 'LTCUSD', 'ETHUSD']
        # passing in self which is this current instance of your algorithm to the  class in this case. In quant connect sometimes they use helper functions instead and dont show the passing of self in
        # in cases where done need the reference to the main algorithm can pass int he QCAlgorithm base class 
        self.pairs = Pair(self, self.universe[0])

class Pair:
    # this shows how the algorithm here is taking in Myalgo_weirdname instance, in quant connect it updates everytime the main algo gets data
    def __init__(self, algorithm, ticker):
        self.newreturns = algorithm.returns
        self.ticker = ticker


will = Myalgo_weirdname()
will.intialize()
print(will.__dict__)
# so we have created some attributes in the algo class, and we have created a pair object which self.pair points to that has more functionality
print(will.pairs.ticker)
# the below is showing how everything in the pair class called is fixed so even if change will.returns, the self.newreturns doesnt change, it will only change if we call are dyamically calling intialize again and changing the self.returns everytime which si what quantconnect does when new data comes in
print(will.pairs.newreturns)
will.returns = 11
print(will.pairs.newreturns)
print(will.__dict__)



# testing super init constructor, if miss out constructor of parent in the super will get thrown an eror
#  so what happens here is the user inputs in the BillAlgorithm class, get passed on those variables to the super(parent) class
#  so in this case when the user types in APPL, and 10 those variables are passe sinto the parent class init function to intialise it, then the price variable we handle it as a modifciatin
class WillAlgorithm:
    def __init__(self, stock, returns):
        self.stock = stock
        self.returns = returns

class BillAlgorithm(WillAlgorithm):
    def __init__(self, stock, returns, price):
        super().__init__(stock, returns)
        self.price = price

chungus = BillAlgorithm("APPL", 10, 999)

print(chungus.__dict__)


# so below here we are passing in the values True and None to the parent class WillAlgorithm2, which stores it under stock and returns
# so super() is just esnetially passign the variables u specifify to the parent init function which will then intialize whatever is there 
# this testign came about due to lesson 10 task 5 of the equity bootcamp quant connect https://www.quantconnect.com/learning/task/174/Using-Fundamental-Data-to-Emit-Insights
# where they passed in true and none into the super, which now I know is just passing variabel to the parent init method
class WillAlgorithm2:
    def __init__(self, stock, returns):
        self.stock = stock
        self.returns = returns

class BillAlgorithm2(WillAlgorithm2):
    def __init__(self):
        super().__init__(True, None)

bigchungus = BillAlgorithm2()

print(bigchungus.__dict__)