# input(): reads a single line of text from the keyboard
# Return a string
# Cna be given a string argument, which is used to prompt the user for input
population = input('Please enter the approximate population in your city: ')
print(type(population))

population = int(population)
print(type(population))
# Can directly write: population = int(input('Please enter the approximate population in your city: '))
