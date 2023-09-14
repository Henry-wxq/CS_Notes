"""
多行注释同时添加或取消：command + /
Key points:
    1) The '>>>' symbol in shell is called: prompt.
    2) Binary Operators: Operators that have two operands
        a) Negation is a unary operator because it applies to one operand
"""

# Negation
print(-5)
print(--5)
print(---5)

# Addition
# When there is a float type in an arithmetic operation, the result will be a float.
print(11 + 3.1)

# Subtraction
print(5 - 19)

# Multiplication
print(8.5 * 4)

# Division
print(11 / 2)
# The result of division always has a decimal point(float) even if the result is a whole number; if we want an int. we
# need to use the integer division: //
print(4 / 2)


# Integer Division
# Python doesn't round the result of integer division. It takes the floor of the result of the division
print(11 // 2)
# Be careful about using negative operands. The result is one smaller than you might expect if the result is negative
# For Python is taking the floor.
print(-17 // 10)
# Floating-point numbers, with //, the result is rounded down to the nearest whole number (the type of the answer if a
# float type as well)
print(3.5 // 1.3)


# Remainder
print(8.5 % 3.5)
# ! When using module, the sign of the result matches the sign of the divisor(the second operand)
print(-17 % 10)
print(17 % -10)
# the relationship between // and % comes from this equation, for any two numbers a and b:
# (b* (a // b) + a % b) is equal to a

# Exponentiation
print(2 ** 5)

'''
Finite Precision: to make calculations fast and memory efficient
'''
print(2 / 3)
print(5 / 3)
print(1 + 2 / 3)

# Take care of the operation order of the arithmetic
print(-2 ** 4)
print(-(2 ** 4))
print((-2) ** 4)
