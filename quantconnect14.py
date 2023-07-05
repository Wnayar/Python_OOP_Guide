class PythonData:
    # they configured somethign here allowing to set like weather["Maxc"] = 3 for example, this is what i came up with to replicate it, their source code for this part was in c#
    # https://www.lean.io/docs/v2/lean-engine/class-reference/PythonData_8cs_source.html
    
    # when gettingitem must return the value
    # note __getitem__ is just a dundeer method alternative for [] indexing into something
    def __getitem__(self, index):
        return self.get_property(index)
    
    # when setting item dont need to return any value
    def __setitem__(self, index, value):
        self.set_property(index, value)
    
    def get_property(self, index):
        return getattr(self, index)

    def set_property(self, index, value):
        # rly intresting issue here if i did the lien fo code below its settign literally index as the new attribute, so have to do it dynamically using the getattr and setattr function
        # self.index= value
        setattr(self, index, value)

class Weather(PythonData):
    def Reader(self):
        weather = Weather()
        weather.Symbol = "Sunshine"
        # THESE TWO LINES HERE WHERE CREATING/INDEXING LIKE THIS IS THE PURPOSE OF THIS QUANTCONNECT 14, REFER TO HELPER CLASS ABOVE
        weather["MaxC"] = 60 
        weather["MinC"] = 20
        return weather

bob = Weather()
print(bob.__dict__)
print()

# return another Weather Object
x = bob.Reader()
print(x.__dict__)
print(isinstance(x, Weather))

x["test"] = 10
value = x["test"]
print(x["test"])
print(x.__dict__)

# this only works now because i set up the getter function 
print(x["Symbol"])



class Random:
    def test(self):
        self.Symbol = "Sunshine"

bob = Random()
bob.test()
print(bob.__dict__)
# this line below will give an error, cant access liek this unless u set up the get method above
# print(bob["Symbol"])