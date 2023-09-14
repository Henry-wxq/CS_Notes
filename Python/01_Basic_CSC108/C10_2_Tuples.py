"""
1) Tuples: an immutable sequence, written using parentheses instead of brackets
"""
# ---------------------------------------- Basic ----------------------------------------
# Can do all the basic operations as other sets
# e.g. slice, 'in', loop over
a = ('a', 'b', 'c', 'd')
print(a[1:])

# Although () represents the empty tuple, a tuple with one elements is not written as (x) but (x, ) with a trailing
# comma to avoid ambiguity
print(type(()))

print(type((5 + 3)))  # int
print(type((5 + 3, )))  # tuple

# python uses the comma as a tuple constructor, so we cna leave of the parentheses
# but can't directly write: type(3, 5)
c = 3, 5
print(type(c))

# ---------------------------------------- Immutable ----------------------------------------
# once a tuple is created, it can't be mutated; however, the objects inside it can still be mutated if itself can
# be mutated
# the references contained in a tuple can't be changed after the tuple has been created
# but the objects referred to may themselves be mutated (graphs in notability)
b = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
# b[0] = ['Brazil', 73.8]
b[0][1] = 80.0
print(b)

# ---------------------------------------- Assigning to Multiple Variables ----------------------------------------
# Python first evaluates all expressions on the right side fo the = symbol, and then it assigns those values to the
# variables on the left side
x, y = 10, 20
print(x)
print(y)

# Python will happily pull apart info out of any collection
[w, x] = {10, 20}
print(w)
print(x)

# swap the values of two variables
d = 'first'
e = 'second'

d, e = e, d

print(d)
print(e)

