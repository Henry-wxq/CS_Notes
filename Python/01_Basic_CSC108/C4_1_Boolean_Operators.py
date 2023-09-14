"""
    1) Control Flow Statements: control the way the computer executes programs
    2) Basic Operators: and, or, not
    3) Relational Operators: creates Bool values in expressions
        a) >: Greater than
        b) <: Less than
        c) >=: Greater than or equal to
        d) <=: Less than or equal to
        e) ==: Equal to
        f) !=: Not equal to
    4) iff: 'if and only if'/ 'exactly when'
    5) Short-Circuit Evaluation: Python looks from left to right; As soon as it knows enough to stop evaluating, it
    stops, even if some operands haven't been looked at yet
    6) ASCII: American Standard Code for Information Interchange
"""
# ---------------------------------------------- Basic Operators ------------------------------------------------
# and: has the second precedence
# Short-Circuit Evaluation: if the first operand is False, the second operand isn't evaluated
# 1 / 0: evaluates as ZeroDivisionError
print((2 > 3) and (1 / 0))


# or: has the third precedence; inclusive: can have both True/False
"""
exclusive or: evaluates to True if and only if exactly one of them is True
>>> a = (b1 and not b2) or (b2 and not b1)
>>> print a

much easier writing: b1 != b2
"""
# Short-Circuit Evaluation: if the first operand is True, the second operand isn't evaluated
print((2 < 3) or (1 / 0))

# not: has the highest precedence
print(not '')

# ---------------------------------------------- Relational Operators ------------------------------------------------
# int and float can be compared with any of the relational operators(int are automatically converted to float)
print(67 != 67)

"""
1) Arithmetic operators have high precedence than relational operators
    a) + and / are evaluated before < or >
2) Relational operators have higher precedence than Boolean operators
    a) < or > are evaluated before and, or, and not.
3) All relational operators have the same precedence
"""
x = 2
y = 5
z = 8
print(x < y and y < z)

# chain the comparisons
print(x < y < z)

# Startling cases: below equals to: print((3 < 5) and (5 != True))
print(3 < 5 != True)

# ---------------------------------------------- Comparing Strings ------------------------------------------------
# The later in alphabetical order, the bigger
print('b' > 'a')

# All the uppercase letters come before all the lowercase letters: 'Z' is less than 'a'
print('A' > 'z')

# When more than one character: comparing from left to right
print('abcd' > 'abc')

# in: checks whether one string appears inside another one
print('Nov' in '22 Nov 2022')

# The empty string is always a substring of every string
print('' in 'abc')
