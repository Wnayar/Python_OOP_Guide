class PythonData:
    # they configured somethign here allowing to set like weather["Maxc"] = 3 for example
    pass

class Weather(PythonData):
    def Reader(self):
        weather = Weather()
        weather.Symbol = "Sunshine"
        # weather["MaxC"] = 3 , mpt too sure, but i guess its soemthign in the pythondataclass
        return weather

bob = Weather()
print(bob.__dict__)
print()

# return another Weather Object
x = bob.Reader()
print(x.__dict__)
print(isinstance(x, Weather))