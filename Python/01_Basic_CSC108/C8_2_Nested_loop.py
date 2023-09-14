"""
1) number of times that function print is len(outer) * len(inner)
"""
# ---------------------------------------- loop over the same list ----------------------------------------
# can only use range as well but the type is then different
def print_table(n):
    num = list(range(1, n + 1))

    for i in num:
        print('\t' + str(i), end='')

    # using print to change the line
    print()

    for num1 in num:

        print(num1, end='')
        for num2 in num:
            print('\t' + str(num1 * num2), sep='')

        print()


print(print_table(5))
# ---------------------------------------- loop over nested and ragged list ----------------------------------------
# nested list: outer and inner list
# ragged list: nested lists with inner lists of varying lengths
