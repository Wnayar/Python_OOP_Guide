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


