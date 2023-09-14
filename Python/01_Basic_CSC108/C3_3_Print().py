# Print doesn't allow any styling of the output: no colors, no italics, no boldface
# all output is plain text

# When printing a string, it prints the values of any escape sequences
print('one\ttwo\nthree\tfour')
"""
different from the file, in shell:
>>> print('one\ttwo\nthree\tfour')
one     two
three   four
"""

# When printing a comma-separated list of values, it prints the values with a single space between them, without comma
print(1, 2, 3)

# Can print any types of value in a single function call
print(True, 1.3, 'two')

# Call print with an expression as an argument
# Because the sep is ' ', so don't need any space in the two strings
radius = 5
print("The diameter of the circle is", radius * 2, "cm.")

# Default Parameters in print(): print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# sep=' ': separate each value with a space'; sep=', ': separate each value with a comma and a space
print('a', 'b', 'c', sep=', ')

# end='\n': end with a new line; end='': end with an empty string
print('a', 'b', 'c', sep=', ', end=', and')
print('d')
print('e')
