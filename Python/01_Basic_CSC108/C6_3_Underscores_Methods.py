"""
1) Any method beginning and ending with two underscores is considered special by Python
2) These methods are typically connected with some other syntax in Python: use of that syntax will trigger a method call
3) Never call these special methods directly, those are just for understanding
"""
# __add__
print('TTA'.__add__('GGG'))

# put a space after -3 in the second instance(with the underscores) so that Python doesn't think we're making
# a float-point number -3
print(3 .__add__(5))
print(-3 .__abs__())
print(3 .__gt__(5))

# Function objects, like other objects, contain double-underscore variables.
# the documentation for each function is stored in a variable called __doc__:
print(abs.__doc__)
print(abs(-3))

