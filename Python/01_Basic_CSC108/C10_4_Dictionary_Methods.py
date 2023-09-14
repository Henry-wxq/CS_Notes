scientist_to_birth = {'Newton': 1642, 'Darwin': 1912, 'Turing': 1912}
copy_scientist_to_birth = {'Newton': 1642, 'Darwin': 1912, 'Turing': 1912}

# D.clear(): removes all key/value pairs from dictionary D; Return None
scientist_to_birth.clear()
print(scientist_to_birth)

# D.get(k): Returns the value associated with key k, or None if the key isn't present; usually use D[k] instead
print(copy_scientist_to_birth.get('Newton'))

# D.get(k, v): Returns the value associated with key k, or a default value v if the key isn't present
# but it won't be added into the dictionary
print(copy_scientist_to_birth.get('Fields', 1863))
print(copy_scientist_to_birth)

# D.keys(): Returns dictionary D's keys as a set-like object = entries are guaranteed to be unique
print(copy_scientist_to_birth.keys())
print(type(copy_scientist_to_birth.keys()))

# D.values(): Returns dictionary D's values as a list-like object - entries may or may not be unique
print(copy_scientist_to_birth.values())
print(type(copy_scientist_to_birth.values()))

# D.items(): Returns dictionary D's (key, value) pairs as set-like objects
print(copy_scientist_to_birth.items())
print(type(copy_scientist_to_birth.items()))

# D.pop(k): Removes key k from dictionary D and returns the value that was associated with k - if k isn't in D,
# an error is raised
print(copy_scientist_to_birth.pop('Newton'))

# D.pop(k, v): Removes key k from dictionary D and returns the value that was associated with k;
# if k isn't in D, returns v
print(copy_scientist_to_birth.pop('Fields', 1863))

# D.setdefault(k): Returns the value associated with key k in D
print(copy_scientist_to_birth.setdefault('Darwin'))

# D.setdefault(k, v): Returns the value associated with key k in D; if k isn't a key in D, adds the key k with the
# value v to D and returns v
print(copy_scientist_to_birth.setdefault('Fields', 1863))
print(copy_scientist_to_birth)

# D.update(other): updates dictionary D with the contents of dictionary other; Return None
# for each key in other, if it is also a key in D, replaces that key in D's value with the value from other
# for each key in other if that key isn't in D, adds that key\value pair to D
add_scientist_to_birth = {'Newton': 1642}
copy_scientist_to_birth.update(add_scientist_to_birth)
print(copy_scientist_to_birth)

# ---------------------------------------- loop over D.item() ----------------------------------------
for key, value in copy_scientist_to_birth.items():
    print(key, 'was born in', value)

# ---------------------------------------- Print the Dictionary Alphabetically ----------------------------------------
sorted_scientist = sorted(copy_scientist_to_birth.keys())
for scientist in sorted_scientist:
    print(scientist, copy_scientist_to_birth[scientist])

# ---------------------------------------- Inverting a Dictionary ----------------------------------------
# There's no guarantee that the values are unique, so we have to handle the collisions
dic = {'a': 1, 'b': 2, 'c': 1}  # should be invert_dic = {1: ['a', 'c'], 2: ['b']}
invert_dic = {}

for key, value in dic.items():
    if value in invert_dic:
        invert_dic[value].append(key)
    else:
        invert_dic[value] = [key]

print(invert_dic)
