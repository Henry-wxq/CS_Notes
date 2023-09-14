"""
1) A set is an unordered mutable collection of distinct items
    a) unordered: items aren't stored in any particular order
    b) distinct: any item appears in a set at most once
"""
# ---------------------------------------- Basic ----------------------------------------
# unordered and distinct
a = {'a', 'b', 'c', 'd', 'd', 'a'}
print(a)

# if they contain the same items, then they are equal
b = {'b', 'c', 'd', 'a'}
print(a == b)

# ---------------------------------------- Function set() ----------------------------------------
# set(): To create an empty set, with no arguments
# Not using {} to create
c = set()
print(type(c))

# if the set is empty, then it will shows: set() instead of {}
print(c)

# set() expects either no arguments or a single argument that is iterable (at most one)
# e.g. list, range, string, set, tuple
d = set([3, 5, 7, 8])
print(d)

e = set('abcdefg')
print(e)

# if we use a set as the argument of the set(), it won't create a nested set
f = set(d)
print(f)

# ---------------------------------------- Sets Methods ----------------------------------------
g = {2, 3, 4, 5, 6, 7}
h = {1, 2, 3}
# S.add(v): adds item v to a set S - this has no effect if v is already in s; Return None
d.add('6')
print(d)

# S.clear(): removes all items from set S; Return None
h.clear()
print(h)

# S.difference(other): returns a set with items that occur in set S but not in set other
# If there are some items in other but not in s, ignore them
print(d.difference(g))

# S.intersection(other): returns a set with items that occur both in sets S and other
print(d.intersection(g))

# S.issubset(other): returns True iff all of set S's items are also in set other
# if s is the same as other, return True, apparently
print(h.issubset(g))
print(g.issubset(g))

# S.issuperset(other): returns True if and only if set S contains all of set other's items
# if s is the same as other, return True, apparently
print(g.issuperset(h))

# s.remove(v): removes item c from set s; Return None
# if v doesn't exist in s: an error occur
d.remove('6')
print(d)

# s.symmetric_difference(other): returns a set with items that are in exactly one of sets S and other - any items that
# are in both sets are not included in the result
print(d.symmetric_difference(g))

# s.union(other): returns a set with items that are either in set S or other (or in both)
print(d.union(g))

# ---------------------------------------- Sets Operations ----------------------------------------
# set1.difference(set2) == set1 - set2
print(d - g)

# set1.intersection(set2) == set1 & set2
print(d & g)

# set1.issubset(set2) == set1 <= set2
print(h <= g)

# set1.issuperset(set2) == set1 >= set2
print(d >= h)

# set1.symmetric_difference(set2) == set1 ^ set2
print(d ^ g)

# set1.union(set2) == set1 | set2
print(d | g)
