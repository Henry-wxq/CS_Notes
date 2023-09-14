"""
Key Points:
    1) General Form of a function call:
        a) <<function_name>>(<<arguments>>)
            § An argument is an expression that appears between the parentheses of a function call.
    2) The rules to executing a function call:
        a) Evaluate each argument one at a time, working from left to right
        b) Pass the resulting values into the function
        c) Execute the function.
"""

# help(): shows documentation for any function
help(abs)

# abs(): produces the absolute value of a number
day_temperature = 3
night_temperature = 10
print(abs(day_temperature - night_temperature))
# The last row of statements is a function call

# int() & float(): convert one type to another
# when a floating number is converted to an integer, it is truncated, not rounded
print(int(24.6))
print(int(-4.3))
print(float(21))

# round(): rounds a floating-point number to the nearest integer
# 四舍六入！！！
print(round(3.3))
print(round(3.5))
print(round(-3.3))
print(round(-3.5))
# round(number[, ndigits])
print(round(3.1415, 2))

# pow(x, y[, z]): (x ** y) % z
print(pow(2, 4, 3))

# id(): track the actual memory address of an object
print(id(day_temperature))
# Function objects also have memory addresses:
print(id(abs))
