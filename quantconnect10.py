# SECTION A

# testing lists additions
templist = [1, 2, 3]
templist1 = [True, False]
templist2 = ["foo"]

# so this just shows you can merge lists together using +
newlist = templist + templist1 + templist2
print(newlist)

for x in templist + templist1 + templist2:
    print(x)



# SECTION B

# some random testing of super(), nothing realy learnt below was just testing
#  intersting points default arguments placed after non default
# techniocally if wanted bar, could just, not put any arguemnt after as already ste to deafult
# in quant connect the dafult is resolution daily, the reason they set the default in Bill class, and Will class, is that if Bill class dint not have a default a error will be thrown saying missing positional argument as it can only look one level up at a time
# refer to lesson 12, sector weighted portfolio construction of equity bootcamp
class Will:
    def __init__(self, rebalance = "yearlyresolution"):
        self.rebalance = rebalance


class Bill(Will):
    def __init__(self, age, rebalance = "bar"):
        super().__init__(rebalance)
        self.age = age

billy1 = Bill(21, "foo")
print(billy1.__dict__)

billy2 = Bill(22)
print(billy2.__dict__)

 

# SECTION C

# just a quick refersher on OOP, cant just randomly write self.age = 21
class test:
     # self.age = 21, this makes no sense, because u need to pass in the instance through a function
    # the way to do the above is usign a constructor, sayign for this instance of the class I want the new age to be ...
    def __init__(self):
        self.newage = 21

    def age(self, number):
        self.age = number
    
baz = test()
baz.age(21)
print(baz.__dict__)





# SECTION D
class Omega:
    def OnSecuritiesChanged(self, changes):
        newchanges = [200 + x for x in changes]
        for x in newchanges:
            print(x)


class Alpha(Omega):
    def OnSecuritiesChanged(self, changes):
        newchanges = [100 + x for x in changes]
        for x in newchanges:
            print(x)



class Beta(Alpha):
    def OnSecuritiesChanged(self, changes):
        for x in changes:
            print(x)
        
        # the reason quantconnect is set up as such callign the super(), is it allow su to modify want to uwant, then u just have to call back the parent function to do whatever else it was meant to do you can read the documentation
        # https://www.quantconnect.com/docs/v2/writing-algorithms/algorithm-framework/portfolio-construction/key-concepts
        #  and on the lean engine source code line 150 onsecuriteschanged https://www.lean.io/docs/v2/lean-engine/class-reference/PortfolioConstructionModel_8cs_source.html
        # super seems to check the parent class, if its not there it will keep checking one level up in the method resolution order
        #  this can be proved by commenting out the function in Alpha and it will call from Omega 
        super().OnSecuritiesChanged(changes)
    
    

chungus = Beta()
chungus.OnSecuritiesChanged([1, 2, 3, 4])