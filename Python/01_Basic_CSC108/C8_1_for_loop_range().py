"""
1) General form: for <<variable>> in <<list/string/......>>:
                     <<block>>
    a) a block is a sequence of one or more statements; each pass through the block is called an iteration

2) Executing Sequence:
    a) The loop variable is assigned the first item in the list, and the loop block is executed
    b) ...... second item ......
    c) ......
    d) ...... last item ......

3) Function range returns a range object, we can create a list based on its values.
"""
# ---------------------------------------- Using existing variable after 'for' ----------------------------------------
# if we use an existing variable, the loop still starts with the variable referring to the first element
# of the list. The content of the variable before the loop is lost, exactly as if we had used an assignment statement to
# give a new valur to that variable
speed = 2
velocity = [3, 5, 7, 9, 11]

for speed in velocity:
    print('Walk or run at', speed, 'km/h')  # because sep = ' ', so don't need any space in the string value.

# ---------------------------------------- for - string ----------------------------------------
name = 'Henry'
for ch in name:
    if ch.isupper():
        print(ch)

# ---------------------------------------- range() ----------------------------------------
# range(i): produces an object that will generate a sequence of integers (from 0(inclusive) to num(exclusive))
print(list(range(10)))

# range(i, j): produces an object that will generate a sequence of integers (from i(inclusive) to j(exclusive))
print(list(range(1, 5)))

# range(i, j, step): the defaulted step size is 1 means 'successively increase by one'
print(list(range(2000, 2050, 4)))
# when step is negative, it produces a descending sequence; and i should be greater than j; otherwise, the result
# is empty
print(list(range(2050, 2000, -4)))

total = 0

for num in range(1, 101):
    total += num

print(total)

# ---------------------------------------- Processing using indices ----------------------------------------
values = [4, 10, 5, 3, 7]

for num in values:
    num *= 2
    print(num)
# Each loop iteration assigned an item in the list values to variable num.
# Doubling that value inside the loop changes what num refers to, but it doesn't mutate the list object
print(values)

for i in range(len(values)):
    values[i] *= 2

# correct approach is to loop over the indices of the list
# len(values): the number of items it contains; range(len(values)): a sequence containing exactly the indices for values
print(values)

# ---------------------------------------- Processing Parallel Lists ----------------------------------------
# These lists are parallel lists, because the item ar index i of one list corresponds to the item at index of the
# other list
fruit = ['peach', 'watermelon', 'durian', 'strawberry']
weight = [0.1, 2, 1.5, 0.01]

# only works when the length of fruit is the same as weight, or an error will occur
for i in range(len(fruit)):
    print(fruit[i], 'is', weight[i], 'kg')
