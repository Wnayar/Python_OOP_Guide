class QCAlgorithm:

    randomclassvariable = 0


# this essentially just falls under class vs instance variables piority 
class BootCampTask(QCAlgorithm):

    def __init__(self):
        pass
    
    # this class variable does nothing it isnt assigned to the instance
    highestSPYPrice = 9


    def OnData(self, currentpricespy):

    # here we overwrite by creating within the instance a variable with the same name as the class variable
    # python will look at the instance for highest piority than the class after if that variabel not in inside which is why this works
    # so in quant connect they set a class variable of highestSPYPrice = 0, so on the first ondata call method, it will realise the class has no self.highestspyprice so it will refer to the class variable, after that every call afterwards refer to the instance variable
        if currentpricespy > self.highestSPYPrice:
            self.highestSPYPrice = 20 
        elif currentpricespy < self.highestSPYPrice:
            self.highestSPYPrice = 1

    # below here is just showing that is used class variable would be different outcome
        # if currentpricespy > BootCampTask.highestSPYPrice:
        #     self.highestSPYPrice = 20 
        # elif currentpricespy < BootCampTask.highestSPYPrice:
        #     self.highestSPYPrice = 1



bill = BootCampTask()
print(bill.__dict__)

bill.OnData(10)
print(bill.__dict__)

bill.OnData(19)
print(bill.__dict__)