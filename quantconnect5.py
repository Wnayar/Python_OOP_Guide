# ignore this import but can use if want to simulate data comign in with sleep() to delay 
from time import sleep

class QCAlgorithm:
    # MOM is the momentum indicator
    def MOM(self, symbolname, timeperiod):
        return self.momclass(symbolname, timeperiod)
    
    class momclass:
        def __init__(self, symbolname, timeperiod):
            self.symbolname = symbolname
            self.timeperiod = timeperiod


class AlphaModel:
    pass 

class MyAlphaModel(AlphaModel):
    def __init__(self):
        self.mom = []

    def OnSecurtiesChanged(self, algorithm, changes):
        for security in changes:
            self.mom.append({"symbol": security, "indicator":algorithm.MOM(security, 12)})

testmodel = MyAlphaModel()

universestocks = ["APPL", "AMZN", "BABA"]
# simulating adding instances of QCAlgorithm() instances in the form of momentum indicators based on each stock in the universe
testmodel.OnSecurtiesChanged(QCAlgorithm(), universestocks)

# so the output should be self.mom list of dicts ofthe securties and their momentum indicators
print(testmodel.mom)
print(testmodel.mom[0]["indicator"].symbolname, testmodel.mom[0]["indicator"].timeperiod )
    
  
# so now just want to test the passing of the qcalgorithm does it make an instance tied to algo or does it create one on called and one again when called in the algo again but this time tied
# well it turns out it creates an instance when u put the class as the argument then gets tied to the name u assign which makes sense
# as seen from the example below the location of both prints are the same
# so techincally if u just created a class in the argument without tying it to the name in the function its loss forever like in the heap memory leak
def logictest(x, randomfunction, randomclass):
    y = x + 1
    testinstance = randomclass
    print(testinstance)
    # randomfunction
    return y

def randomfunction():
    print("Hello World")

class randomclass:
    def __init__(self):
        print(self)


print(logictest(4, randomfunction(), randomclass()))