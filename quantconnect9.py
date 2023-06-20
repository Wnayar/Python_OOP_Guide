class data:

    def get(self, data):
        self.datatest = data

    # getter @property set here so can call Values function without the ()
    @property
    def Values(self):
        templist = []
        # here .values() is not defined so due to method resolution order it inherits from the above class which in the case looks at inbuilt
        # I am guessing this is what quantconnect does with the .Values call here in tiingo lesson 11 as not specified, but its essentially geting all the values from the dict which in this case are list and going over the list to get the articles
        for listofarticle in self.datatest.values():
             for article in listofarticle:
                templist.append(article)
        return templist


# this would be a segement of a tiingo newsobject except it would have a lot more properties other than the description one which i have here 
class Altobject:
    def __init__(self, description):
        self.Description = description

altobject1 = Altobject("APPL good")
altobject2 = Altobject("APPL is amazing")
altobject3 = Altobject("BABA is very good")
altobject4 = Altobject("BABA is okay")

altnews = data()
altnews.get({"altAPPL":[altobject1, altobject2], "altBABA":[altobject3, altobject4]})

for individualarticles in altnews.Values:
        print(individualarticles.Description)


# testing .items() from tiingo documentation in quantconnecy
tempdict = {"altAPPL":[altobject1, altobject2], "altBABA":[altobject3, altobject4]}
print(tempdict.items())
# .items() offers a view of the dict, which is a list of tuples 
for symbol, listofobjects in tempdict.items():
     for objectsnews in listofobjects:
        print(symbol, objectsnews.Description)