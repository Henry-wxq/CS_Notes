"""
Key Points:
    1) Variable: a name that refers to a value
        a) can use letters, digits, and the underscore symbol (but they can't start with a digit e.g. can't be 777)
    2) Computer Memory:
        a) every location in the computer's memory has a memory address.
        b) mark every memory address with an id prefix
    3) Assignment Statement: <<variable>> = <<expression>>
        a) Evaluate the expression on the right of the = sign to produce a value. This value has a memory address
        b) Store the memory address of the value in the variable on the left of the =. Create or just reuse the
        variable, replacing the memory address that it contains.
"""

# Assignment Statement
# Value 26.0 has the memory address id1; The object at the memory address id1 has type float and the value 26.0;
# Variable degrees_celsius contains the memory address id1; Variable degrees_celsius refers to the value 26.0.
degrees_celsius = 26.0
print(degrees_celsius)

# Assigning a value to a variable that already exists doesn't create a second variable. The existing variable is reused.
degrees_celsius = 0.0
print(degrees_celsius)

# Assigning to a variable doesn't change any other variable.
plus_5 = degrees_celsius + 5
degrees_celsius = 100
print(plus_5)
print(degrees_celsius)



