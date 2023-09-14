"""
1) Dictionary(map): an unordered mutable collection of key/value pairs
    a) The keys form a set:
        § any particular key cna appear once at most in a dictionary;
        § keys are immutable, but the values associated with them don't have to be
2) Looping over dictionary:
for <<variable>> in <<dictionary>>:
    <<block>>
"""
# ---------------------------------------- Basic ----------------------------------------
# creat a dictionary
a = {'Canada Goose': 3, 'Northern Fulmar': 1}

# create an empty dictionary
b = {}

# ---------------------------------------- Index the dictionary ----------------------------------------
# get the value associated with a key
print(a['Canada Goose'])

# Indexing a dictionary with a key it doesn't contain produces an error, like an out-of-range index
# print(a['bird'])

# D[key] = value: update the value associated with a key
# if the key is already in the dictionary, this assignment statement changes the value associated with it
# if the key isn't present, the key/value pair is added to the dictionary
a['Snow Goose'] = 33
a['Eagle'] = 9
print(a)

# ---------------------------------------- del D[key] ----------------------------------------
# del D[key]: remove an entry from a dictionary
del a['Snow Goose']
print(a)

# ---------------------------------------- 'in' operator ----------------------------------------
print('Eagle' in a)

# The in operator only checks the keys of a dictionary
print(9 in a)

# ---------------------------------------- Looping over Dictionary ----------------------------------------
# the loop variable is assigned each key from the dictionary in turn
# the dictionary is unordered
for bird in a:
    print(bird, a[bird])
