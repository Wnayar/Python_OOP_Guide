# The Qaunt connect documentation in python consists of function annotations as a means to highlight what the paramter and return values are, here I will explore this concept
# https://peps.python.org/pep-3107/
# https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions maximouse response on stackoverflow

# just setting y default value to 5 just to show how the annotations come right after the variable, also the annotations are ignored by interpretator
#  meaning even thou I say x should be a string it has no meanign its just letting the user know
def sum (x: str, y: int = 5) -> int:
    # below is called a docstring in python """ """, it was used mostly in python 2 to specify the paramters and return values
    # once python3 came out now we more commonly use function annotations to specify the  
    """
    param x: int
    param y: int
    param return: int
    """
    return x + y

# annotations function is used to show the annotations in a dict format
print(sum.__annotations__)

# doc function which were used in doct string just shows what was wrriten as is 
print(sum.__doc__)