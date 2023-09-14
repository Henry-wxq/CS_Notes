"""
1. General form of a function definition:
    1) def <<function_name>>(<<parameters>>):
           <<block>>
2. Notice:
    1) Can't have two functions with the same name;
    2) the function body must contain at least one statement
3. 'return' statement:
    1) return <<expression>>
    2) evaluates the expression and then produces the result of that expression as the result of the function call
4. Local Variables: variables within a function.
    1) LV created each time that function is called, and erased when the function returns
5. Variable's Scope: the area of a program that a variable can be used in
    1) The scope of a local variable is from the line in which it is defined up until the end of the function.
"""


def calculate_tax(bill: float, tax_rate: float) -> float:  # Function header: names to make easy for readers
    # expected two empty lines above the function header
    # two spaces before inline comments
    # Type Contract: Being involved in the function header, this one, (float, float) -> float
    # Description: Start with the word 'Return'; mention every parameter in the description and
    # describe the return value.
    # Example calls and return values as we would expect to see in the Python Shell.
    """
    Return the amount of tax due on a bill calculated at tex_rate.

    Precondition: 0.0 <= tax_rate <= 1.0

    >>> calculate_tax(10.5, 0.2)
    2.1
    >>> calculate_tax(2000.0, 0.0)
    0.0
    """

    return bill * tax_rate  # the body of the function


print(calculate_tax(20.0, 0.3))  # There expect two lines after the defining function


# When calling the function by using help(), it will exactly reveal what we write in the description!
if __name__ == '__main__':
    help(calculate_tax)

# if we don't have a return statement in a function, nothing is produced, it will reveal: None, as to signal the absence
# of a value


def f(x):
    x *= x + 1


print(f(1))
# when we assign a variable to the f(x), although the result is None, it still has the id
a = f(3)
print(a)
print(id(a))
