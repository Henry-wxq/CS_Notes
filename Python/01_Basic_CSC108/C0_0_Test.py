# Print every multiple of 7 between 3 and 300 (inclusive), in reverse order

for n in range(300, 2, -1):   # start at 300, go down to 3
    if n % 7 == 0:
        print(n)
