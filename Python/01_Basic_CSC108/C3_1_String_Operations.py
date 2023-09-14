"""
1) EOL stands for 'end of line'
2) The order of operands affects the error message
    a) which type does Python saw first, when doing operations between them, it expects the following to be in the same
    type
"""

# ---------------------------------------- len() ----------------------------------------
# Built-in function: len()
# returns the number of characters between the quotes.
# counts any spaces & punctuations; start with 1
print(len('Albert Einstein!'))  # 16
# when two symbol represent a single character, the length of an escape sequence is one
print(len('\''))  # 1

# ---------------------------------------- Add Two Strings ----------------------------------------
# Add two strings: + (concatenation operator)
# adding an empty string to another string produces a new string that is just like the nonempty operand
print("Henry Wei" + '')

# ---------------------------------------- Repeat the String ----------------------------------------
# Repeat the string: *
print('AT' * 5)
# when integer is less than or equal to zero, the operator yields the empty string
print('TATA' * 0)
print('Henry' * -3)

# ---------------------------------------- Convert the String ----------------------------------------
# Convert other types into string: str()
print(str(7))
print(str(7.5))
print(str(True))  # 'True'

# ---------------------------------------- Convert String to other Types ----------------------------------------
# Convert string to other types
print(int('0'))
print(float('56.4'))
print(bool(36))  # 'True'

# ---------------------------------------- Slicing String ----------------------------------------
a = '1234567'

# a[i, j, step]: slice begin from i(inclusive) to j(exclusive); step: take from i1 and go the number of step from i1
# and take i2 and so on
# when j > len(a), no worries, just take when a ends
# a[:]: take the whole string
b = a[1:9:2]
print(b)

# when step < 0, i should > j, and it takes begin from i; j still exclusive
c = a[8:1:-1]
print(c)

# a great way to reverse the string: a[::-1]
d = a[::-1]
print(d)

# when a[i, j, step]: step > 0, and 'i' is -1 (the last index), then it will return an empty string;
# step < 0, and 'i' is 0 (the first index), then it will return an empty string; no error will occur
e = a[-1:-2:1]
f = a[:10:-1]
print(e)
print(f)
