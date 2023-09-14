"""
Type: every value in Python has a particular type. In computing, a type consists of two things; a set of values,
    and a set of operations that can be applied to those values.
    1) int (short for integer): 4 and 17
    2) float (floating-point number): 2.5 and 17.0
        a) When an expression's operands are an int and a float, Python automatically converts the int to a float.
        b) 17.0 = 17. but it's a bad style
    3) str (short for string): 'anything here'
        a) Putting either single or double quotes around it.
        b) The shortest string is the empty string: ''; ""
    4) bool (short for boolean)
        a) Only have two values: True and False
        b) numbers with Bool: Python treats 0 and 0.0 as False and treats all other numbers as True
        c) strings with Bool: Python treats empty string as False and all other string as True
        d) None is also treated as False
    5) module: a collection of variables and functions that are grouped together in a single file.
        a) those variables and functions are usually related
        e.g. module math contains the variable pi and mathematical functions such as cos and sqrt
    6) any class is a type
    7) list(basic sequence type): [<<expression1>>, <<expression2>>, ... , <<expressionN>>]
        a) expty list: []
        b) The list itself is an object, but it also contains the memory addresses of fourteen other objects.
         (15 in total including itself).
        c) lists are heterogeneous: list can contain any type of data even other lists
    8) range(basic sequence type): represents an immutable sequence of numbers and is commonly used for looping a
     specific number of times in for loops
        a) class range(stop)
        b) class range(start, stop[, step])
        c) range is an iterable object but not an iterator


"""

# ---------------------------------------- Bool ----------------------------------------
print(not 0)
print(not 5)
print(not '')
print(not 'bad')
print(not None)

# ---------------------------------------- list ----------------------------------------
Henry = [20031118, 'Male', 'UOT', 'Math']
