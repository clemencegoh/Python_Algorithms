import math

"""
Rounds to nearest 5
Replace base accordingly to switch which 
number to round to
"""
def myround(x, base=5):
    return base * math.ceil(x/base)