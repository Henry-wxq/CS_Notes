"""
1) Alias: an alternative name for sth.
    a) In python two variables are said to be aliases when they contain the same memory address
    b) when we modify the list using one of the variables, its alias shows the change as well
2) Aliasing only happens when a type is mutable
    a) if x and y refer to the same list, then any changes you make to the list through x will be 'seen' by y
    b) this can happen with immutable values like strings.
"""
a = ['Henry', 'Chloe', 'Lake', 'Kevin', 'Calvin']
# ---------------------------------------- Slicing List ----------------------------------------
# list[i:j]: first index i is inclusive and last index j is exclusive (a lice of the original list from index i up to
# but not including j)
# first index can be omitted if we want to slice from the beginning of the list, and last as well.
print(a[1:3])
print(a[1:5])

# To create a copy of the entire list, omit both indices (This is not an alias when using slice!)
# a_copy has the same items, bit lists themselves are different objects at different memory addresses.
a_copy = a[:]
print(a_copy)

# ---------------------------------------- List Aliasing ----------------------------------------
# (picture in note)
b = a
a[3] = 'Kavin'
print(a)
print(b)


def remove_name(l1: list) -> None:
    """
    :param l1: the list contain names
    :return: remove the last item from L

    >>> remove_name(['Tom', 'Bob'])
    """
    del l1[-1]


remove_name(a)
# When the call on function remove_name is executed, parameter l1 is assigned the memory address that 'a'
# contains. That makes l1 and 'a' aliases. When the last item of the list that L refers to is removed, that
# change is 'seen' by 'a' as well.
# Therefore, the modified list doesn't actually need to be returned
print(a)
