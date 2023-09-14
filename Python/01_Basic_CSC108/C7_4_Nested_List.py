"""
1) Assigning a sublist to a variable creates and alias for that sublist
    a) Any directly assigning list to a variable will create an alias; only two ways can eliminate this
"""
a = [['Henry', 'Bob', 'Tony', 'Calvin'], ['Jane', 'Chloe', 'Lake']]

# ---------------------------------------- Chain the rules ----------------------------------------
# We can chain together method calls or nest function calls
a[1].sort()
print(a)
