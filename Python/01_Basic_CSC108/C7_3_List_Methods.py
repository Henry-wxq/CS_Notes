"""
1) Lists are objects and thus have methods
2) All the methods shown below modify the list instead of creating a new list
3) Methods that mutate a collection, such as append and sort, return None, be careful!
4) Two ways to copy a list:
    a) b = a.copy() (.copy(): method)
    b) b = a[:] (slicing)
"""
a = ['Henry', 'Chloe', 'Lake', 'Kevin', 'Calvin']
b = ['Bob', 'Tom', 'Tony', 'Jane']

# ---------------------------------------- .append(v) ----------------------------------------
# L.append(v): appends value v to list L
c = a.append('Kavin')
print(a)

# some methods only modifies the list and return nothing; so when we directly print it out, we will get None
print(a.append('Kavin'))
print(c)

# ---------------------------------------- .extend(v) ----------------------------------------
# L.extend(v): appends the items in v to L (v is a list here)
a.extend(b)
print(a)

# it's different from using '+': '+' creates a new list but .extend(v) doesn't
print(id(a + b))
print(id(a))


# ---------------------------------------- .clear() ----------------------------------------
# L.clear(): removes all items from list L
b.clear()
print(b)

# ---------------------------------------- .count(v) ----------------------------------------
# L.count(v): returns the number of occurrences of v in list L
print(a.count('Henry'))

# ---------------------------------------- .index(v) ----------------------------------------
# L.index(v): returns the index of the first occurrence of v in L - and error is raised if c doesn't occur in L
print(a.index('Chloe'))

# ---------------------------------------- .index(v, beg, end) ----------------------------------------
# L.index(v, beg, end): returns the index of the first occurrence of v between indices beg(inclusive) and
# end(exclusive) in L; and error is raised if v doesn't occur in that part of L
print(a.index('Lake', 2, 4))

# ---------------------------------------- .insert(i, j) ----------------------------------------
# L.insert(i, v): inset value v at index i in list L, shifting subsequent items to make room
a.insert(1, 'Michelle')
print(a)

# ---------------------------------------- .pop() ----------------------------------------
# L.pop(): Removes and returns the last itme of L (which must be nonempty)
print(a.pop())
print(a)

# ---------------------------------------- .remove(v) ----------------------------------------
# L.remove(v): removes the first occurrence of value v from list L
a.remove('Michelle')
print(a)

# ---------------------------------------- .reverse() ----------------------------------------
# L.reverse(): reverses the order of the values in list L
a.reverse()
print(a)

# ---------------------------------------- .sort() ----------------------------------------
# L.sort(): sorts the values in list L in ascending order (for strings with the same letter case, it sorts in
# alphabetical order)
a.sort()
print(a)

# ---------------------------------------- .sort(reverse=True) ----------------------------------------
# L.sort(reverse=True): Sorts the values in list L in descending order
a.sort(reverse=True)
print(a)

# ---------------------------------------- .copy() ----------------------------------------
# L.copy(): return the copy of list L which is not an alias of L
print(a.copy())

d = a.copy()
a.clear()
print(d)
