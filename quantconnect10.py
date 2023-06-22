# testing lists additions
templist = [1, 2, 3]
templist1 = [True, False]
templist2 = ["foo"]

# so this just shows you can merge lists together using +
newlist = templist + templist1 + templist2
print(newlist)

for x in templist + templist1 + templist2:
    print(x)



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