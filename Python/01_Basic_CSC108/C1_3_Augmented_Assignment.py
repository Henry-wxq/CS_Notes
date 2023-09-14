"""
Key Points:
    1) Augmented Assignment: combines and assignment statement with an operator to make the statement more concise.
        a) Procedure:
            § Evaluate the expression on the right of the sign = sign to produce a value (extremely important, do the
            evaluation at the right first)
            § Apply the operator attached to the = sign to the variable on the left of the = and the value that was
            produced. This produces another value. Store the memory address of that value in the variable on the left
            of the =
        b) Note that the operator is applied after the expression on the right is evaluated
    2) Errors:
        a) Syntax Errors: happen when typing sth. isn't valid Python code
            § >>> 2 +
            § >>> 12 = x
        b) Semantic Errors: happen when telling Python to do something that it just can't do, like divide a number by
        zero
            § >>> 3 + moogah
    3) Split a statement into more than one line (do one of two things):
        a) Make sure your line break occurs inside parentheses, or
            § >>> (2 +
              ... 3)
        b) Use the line-continuation character, which is a backslash, \.
            § >>> 2 + \
              ... 3
"""

# Shorthand version of operators
x = 7
# += (x = x + 2)
x += 2
print(x)

# -=
x = 7
x -= 2
print(x)

# *=
x = 7
x *= 2
print(x)

# /=
x = 7
x /= 2
print(x)

# //=
x = 7
x //= 2
print(x)

# %=
x = 7
# x = x % 2
x %= 2
print(x)

# **=
x = 7
x **= 2
print(x)

# Note that the operator is applied after the expression on the right is evaluated
d = 2
d *= 3 + 4
print(d)
