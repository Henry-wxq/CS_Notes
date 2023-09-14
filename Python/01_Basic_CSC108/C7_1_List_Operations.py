"""
1) the objects are mutable, the contents of a list can be mutated
2) however, numbers and string are immutable. Methods that appear to do that, like upper, actually create new strings
    a) so it's only possible to use an expression of the form s[i] on the right side of the assignment operator

"""
a = [1, 2.3, 4, 'Henry']
b = [1.5, 2, 4.5, 6, True]
c = [1, 2, 3]
f = [[1, 2], [3, 4]]
# ---------------------------------------- Index a list ----------------------------------------
# first item is at index 0, the second at index 1
# the last item is at index -1
# empty list has no items
print(a[0])
print('His name is ', a[-1])

# ---------------------------------------- Modifying a list(doesn't crate new) ----------------------------------------
# assign a new value to a specific element of the list by index
# a[1] behaves like a simple variable which can be either on the left or right side of =
# left: look up the memory address at index i of list L, so it can be overwritten
# right: get the value referred to by the memory address at index i of List L
a[1] = 2
print(a)

# del L[i]
del c[0]
print(c)

# ---------------------------------------- Operations on list(create new) ----------------------------------------
# len(L): returns the number of items in list L
print(len(a))

# max(L): returns the maximum value in list L
# doesn't work when a string exists in the list; but work when there is a Boolean value, which represent 1 as True and
# 0 as False
# but when printed out, it's bool value but not 1 or 0
print(max(b))

# min(L): returns the minimum value in list L
print(min(b))

# sum(L): returns the sum of the values in list L
# if there is any float number, then return float for the final answer
print(sum(b))

# sorted(L): returns a copy of list L where the items are in order from smallest to largest (does not mutate L)
# can't use when a string element exists
d = sorted(b)
print(d)
print(b)

# L1 + L2: lists can be combined using the concatenation operator (different from .extend() method as this
# need to create a new list)
# L1 and L2 need to be the type list
e = a + b
print(e)

# L1 * int: get a new list containing the elements form the original list repeated that number of times
print(a * 3)

# ---------------------------------------- 'in' Operator ----------------------------------------
# object in L: be applied to list to check whether an object is in a list
print(True in b)

# only checks for a single object; it doesn't check for object in the sublist
print(1 in f)
print([1, 2] in f)
