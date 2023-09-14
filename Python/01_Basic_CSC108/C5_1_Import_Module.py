"""
1) dir(MODULE): what functions and variables are available(help() will show how to use them)
"""
# ---------------------------------------- Importing Module ----------------------------------------
# importing a module creates a new variable with that name whose type is module
import math
print(type(math))

# from MODULE import xxxxxx: specify exactly what you want to import from a module
# This doesn't introduce a variable called math. Instead, it creates function sqrt and variable pi in the
# current namespace
from math import sqrt, pi
r = 5
print('circumference is', 2 * pi * r)
print(sqrt(9))

# from MODULE import *: brings in every thing from the module
from math import *

# can use build-in function help() to see what it contains
help(math)

# ---------------------------------------- dot operator ----------------------------------------
# dot: look up the object that the variable to the left of the dot refers to and in that object, find the name that
# occurs to the right of the dot
print(math.pi)

# ---------------------------------------- Restoring a Module ----------------------------------------
math.pi = 3
import imp
math = imp.reload(math)

# ---------------------------------------- Module __builtins__ ----------------------------------------
# _builtins_: contains Python's built-in functions
print(dir(__builtins__))
