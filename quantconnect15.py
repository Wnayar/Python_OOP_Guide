# SECTION A: logic flow
# https://youtu.be/yuZBBX47xK0 , from a-z tut 13 quantconnect
# side notes: return stements can only be written within a function, which makes sense of course how can you be returning without beign withing something

def OnData(foo):
    for pair in foo:
        if type(pair) == int:      
            if pair < 2:
                print("if", pair)
            elif pair >=2 and pair <=3:
                print("elif", pair)
            # by putting the conitnue here we go to the next iteration so the number 4 doesnt get evaluted
            # because if its an int and doesnt fall in the first two if and elif will go to conitnue next loop
            continue
            
        # so the 4 ehre never gets checked with the conitnue in place as the first if takes in all ints
        if type(pair) == bool or pair == 4: 
            print("continue", pair)

        else:
            print("else", pair)

x = [1, 2, 3, 4, False, True, 6, 7, "foo", "bar"]
OnData(x)



# SECTION B: Intialize a list of assets by utilising a class and how the rteurn values work
class QCAlgorithm():
    def symbols(self, symbol):
        print("Hi")
        self.symbol = symbol + "cryptopair"
        return self.symbol

class CustomAlgo(QCAlgorithm):
    def Initialize(self):
        self.minimumVolume = 1000000
        universe = ['BTCUSD', 'LTCUSD', 'ETHUSD']
        # so this means we have created a list of CyrptoPair objects, which we set the symbol and min volume for, and in quant connect tthey add the data here too etc
        self.pairs = [CryptoPair(self, ticker, self.minimumVolume) for ticker in universe]
        # so this shows we are passing in our algo as self to the cryptopair class
        #  we do this so we can modify our algo and use the helper function from the qcalgorithm class in the cryptopair class 
        print(self)

class Random:
    count = 0
    def __init__(self, number):
        self.number = number + Random.count
        Random.count += 1
    
    def update(self):
        self.number += 1


class CryptoPair:
    def __init__(self, algorithm, ticker, minimumVolume):
        self.ticker = algorithm.symbols(ticker)
        self.minimumVolume = minimumVolume
        self.randomobject = Random(1)

        
cryptostrategy = CustomAlgo()
cryptostrategy.Initialize()
# so this means we have created a list of CyrptoPair objects, which we set the symbol and min volume for, and in quant connect tthey add the data here too etc
print(cryptostrategy.pairs[0].ticker)
print(cryptostrategy.pairs[0].minimumVolume)
print(cryptostrategy.pairs[0].__dict__)
print(cryptostrategy.pairs[0].randomobject.__dict__)
print(cryptostrategy.pairs[0].randomobject.__dict__)
cryptostrategy.pairs[0].randomobject.update()
print(cryptostrategy.pairs[0].randomobject.__dict__)


# okay so this is very intresting the above was inspired by tryign to understand why in quantconnect when this is written:
# class Pair:
    # def __init__(self, algorithm, ticker, minimumVolume): 
    #     self.symbol = algorithm.AddCrypto(ticker, Resolution.Daily, Market.Bitfinex).Symbol
# and everytime in the ondata when the symbol is called:
    # def OnData(self, data):
        
    #     for pair in self.pairs: 
    #         if not pair.rsi.IsReady:
    #             return
            
    #         symbol = pair.symbol
    #         rsi = pair.rsi.Current.Value 

# the main point of concern was doesnt this mean im adding algorithm everytime?
#  the answeer is no self.symbol which was created on the init is storing the symbol value alone
# so you can think of it as static as the init is only called on construction once

#  but then it gets confusing when you look below at the rsi indicators as such:
# class Pair:
#     def __init__(self, algorithm, ticker, minimumVolume): 
#         self.symbol = algorithm.AddCrypto(ticker, Resolution.Daily, Market.Bitfinex).Symbol
#         self.rsi    = algorithm.RSI(self.symbol, 14,  MovingAverageType.Simple, Resolution.Daily)
# and in the OnData method
    # def OnData(self, data):
        
    #     for pair in self.pairs: 
    #         if not pair.rsi.IsReady:
    #             return
            
    #         symbol = pair.symbol
    #         rsi = pair.rsi.Current.Value 
            
    #         if self.Portfolio[symbol].Invested:
    #             if not pair.Investable():
    #                 self.Liquidate(symbol, "Not enough volume")
    #             elif rsi < self.rsiExitThreshold:
    #                 self.Liquidate(symbol, "RSI below threshold")
    #             continue
# so then you might be wondering how can they allocate a dynamic sort of thign to somethign created int eh consructor
# well the answer is simple the return value of the self.rsi is not symbol which si static, we are returning the whole rsi object
# so self.rsi is static int he sense its always pointing to the same rsi object this never changes, but withing the RSI object for example quantconnect can have methods called which update th eproperties
#  so for exampel when u call rsi.Current.Value you are eitehr callign a properrty or fucntion which is trackign the most current value, it si prob beign updated inetrnally
# i replciated htis with my update function in my random class above

# so logn sorty shorts, when im calling self.symbol im not calling that function addcrypto, im just callign the symbol retruned value which i set out on construction, that function add crypto is only calle donce on construction 
# which si why its very smart to intialize the pairs to be traded through a class like tgis, its very efficeint


# SECTION C: Exploring assigning function to a variable
def chungus():
    print("foobarbaz")
    return 5

chungus()
x = chungus
x()
x = chungus()
print(x)

y = chungus
print(y)
print()

z = chungus()
print(z)
#  so this just simply means when creating the z variable we call the chungus variable
# which then stores the value 5 into z
#  so when we call z from now on its just a number, which cna be proved below
print(isinstance(z, int))
# thus whenever quant connect isintializing such as this:
# class Pair:
#     def __init__(self, algorithm, ticker, minimumVolume): 
#         self.symbol = algorithm.AddCrypto(ticker, Resolution.Daily, Market.Bitfinex).Symbol
# all thsi means is we are callign the functin add crypto once, then we store the symbol value into self.symbol, so form now on self.symbol just refers to the symbol
    # def OnData(self, data):
        
    #     for pair in self.pairs: 
    #         if not pair.rsi.IsReady:
    #             return
            
    #         symbol = pair.symbol
    #         rsi = pair.rsi.Current.Value 
# so that means whever u call .symbol from nwo it just refers to that stored symbol valeu u are nto calling the function again 
# if u wanted to store a function to a variable which can be called u woudl have to do x = function, then call the function with x()
# so on construction the values gets fixed , u nless u udpate them, the value can also be pointers to objects, and withign those objects u can do as you please in teh future such as update the rsi values