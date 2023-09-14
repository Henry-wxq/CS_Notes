"""
1) used when don't know in advance how many loop iterations is to execute
2) general form: while <<expression>>:
                     <<block>>
    a) <<expression>> is sometimes called the loop condition, like the condition of an if statement; if
     that expression evaluates to False, that is the end of the execution of the loop; if the expression
      evaluates to True, the loop body will be executed once then goes back to the top.
"""
# ---------------------------------------- example of while loop ----------------------------------------
time = 0
population = 1000
growth_rate = 0.21
while population < 2000:
    population += growth_rate * population
    print(round(population))
    time = time + 1

print()

# ---------------------------------------- infinite loop ----------------------------------------
# while population != 2000:
#     population += growth_rate * population
#     print(round(population))
#     time = time + 1

# ---------------------------------------- loop based on the input ----------------------------------------
# Since the loop condition checks the value of text, we have to assign it a value before the loop begins
text = ''
while text != 'quit':
    text = input("Please enter your option (or 'quit' to exit): ")
    if text == 'quit':
        print('exiting program......')
    elif text == 'Next':
        print('Approaching......')
    else:
        print('Unknown Command......')

