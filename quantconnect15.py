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



# SECTION B: Intialize a list of assets by utilising a class
class QCAlgorithm():
    def symbols(self, symbol):
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



class CryptoPair:
    def __init__(self, algorithm, ticker, minimumVolume):
        self.ticker = algorithm.symbols(ticker)
        self.minimumVolume = minimumVolume

        
cryptostrategy = CustomAlgo()
cryptostrategy.Initialize()
# so this means we have created a list of CyrptoPair objects, which we set the symbol and min volume for, and in quant connect tthey add the data here too etc
print(cryptostrategy.pairs[0].ticker)
print(cryptostrategy.pairs[0].minimumVolume)