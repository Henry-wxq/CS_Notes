"""
1) General form of a method call:
    <<expression>>.<<method_name>>(<<arguments>>)
2) Steps for executing a method call:
    a) Evaluate <<expression>> as the object
    b) Evaluate the <<arguments>>
    c) Pass the object and argument values into the method
    d) Execute the method
3) Object-Oriented: To describe the style of programming where the objects are the main focus
"""
from math import pi
# ---------------------------------------- String Methods ----------------------------------------
a = 'Henryy'
b = 'enriqueW'
c = '      CCh   hloe      '

# str.capitalize(): Returns a copy of the sting with the first letter capitalized and the rest lower case
# if other letters are capitalized, then will be changed into lower case
print(a.capitalize())
print(b.capitalize())
print(c.capitalize())

# str.count(s): Returns the number of non-overlapping occurrences of s in the string
# s should be a string
print(a.count('y'))

# str.startswith(beginning): Return True iff the string starts with the letters in the string beginning - this is
# case-sensitive
print(a.startswith('H'))

# str.endswith(end): Returns True iff the string ends with the characters in the end string - this is case-sensitive
print(a.endswith('enryy'))

# str.find(s, beg, end): Returns the index of the first occurrence of s in the string, or -1 if s doesn't
# occur in the string - the first character is at index 0. This is case-sensitive.
# beg: the first occurrence of s at or after index beg in the string
# end: the first occurrence of s between indices beg(inclusive) and end(exclusive)
print(a.find('y'))
print(a.find('y', 4, 5))

# str.format(<<expressions>>): Returns a string made by substituting for placeholder fields in the string - each field
# is a pair of braces, '{' and '}', with an integer in between;
# The expression arguments are numbered from left to right starting at 0
# Each field is replaced by the value produced by evaluating the expression whose index corresponds with the integer in
# between the braces of the field. if an expression produces a value that isn't a string, the at value is converted
# into a string
print("{0} is the same as {1}".format(a, b))
# {0: .2f}: In first argument, the number should be formatted as a floating-point number with two digits to the right
# of the decimal point.
print("Pi rounded to {0} decimal places is {1: .2f}]".format(2, pi))
# When omit the position number in {}, then the arguments passed to format replace each placeholder field in
# order from left to right
print("Pi rounded to {} decimal places is {: .2f}]".format(2, pi))

# str.islower(): Returns True iff all characters in the string are lowercase
print(a.islower())

print(b.isupper())

# str.lower(): Turns a copy of the string with all letters converted to lower case
print(a.lower())

print(a.upper())

# str.strip(): Returns a copy of the string with leading and trailing whitespace removed
# Those \n, \t will also be removed; but those whitespaces inside the string is unaffected
print(c.strip())

# str.strip(s): Returns a copy of the string with leading and trailing occurrences of the characters in s removed
# upper and lower case should be the same as s
# should eliminate any white space and only delete when the letter matches s
# will remove all if the matched s is successive
print(a.strip('y'))

# str.lstrip(): Returns a copy of the string with leading whitespace removed
print(c.lstrip())

# str.lstrip(s):Returns a copy of the string with leading occurrences of the characters in s removed
print(a.lstrip('H'))

# str.rstrip(): Returns a copy of the string with trailing whitespace removed
print(c.rstrip())

# str.rstrip(S): Returns a copy of the string with trailing occurrences of the characters in s removed

# str.replace(old, new): Returns a copy of the string with all occurrences of substring old replaced with string new
print(c.replace('h', 'l'))

# str.split(): Returns the whitespace-separated words in the string as a list
print('I am Henry'.split())

# str.swapcase(): Returns a copy of the string with all lowercase letters capitalized and all uppercase
# letters made lowercase
print(a.swapcase())

# ---------------------------------------- Combined Methods ----------------------------------------
# Because c.lstrip is an expression, we can immediately call method lstrip on the result of that expression etc.
print(c.lstrip().lstrip('C').swapcase())
