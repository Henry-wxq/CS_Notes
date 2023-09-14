"""
1) All of these techniques work starting at the current file cursor
2) When the file cursor is at the end of the file, functions read, readlines, and realine all return an empty string.
In order to read the contents of a file a second time, you'll need to close and reopen the file
"""
# ---------------------------------------- The read technique ----------------------------------------
# When want to read the contents of a file into a single string
# When want to specify exactly how many characters to read
with open('C9_0_0_File_Sample_1.txt', 'r') as file1:
    contents1 = file1.read()  # When calling no arguments, it reads everything from the current file

print(contents1)

with open('C9_0_0_File_Sample_1.txt', 'r') as file2:
    contents2 = file2.read(5)  # When called with one integer argument, it reads that many characters and moves the
    # file cursor after the characters that were just read
    the_rest = file2.read()  # Reads the rest of the file; won't start from the beginning

print('The first 5 characters:', contents2)
print('The rest of the file:', the_rest)

# ---------------------------------------- The readlines Technique ----------------------------------------
# It splits up the lines into a list of strings.
with open('C9_0_0_File_Sample_1.txt', 'r') as file3:
    lines1 = file3.readlines()

# Each line ends in \n characters; Python doesn't remove any characters from what is read; it only splits them into
# separate strings
print(lines1)

# If we want to eliminate the \n character, we can use 'for loop' to iterate the list and use
# .strip() or .rstrip() or .lstrip() on the string based on the condition
for line in lines1:
    print(line.strip())

# We can also use built-in function reversed() and sorted() on the list
for line in reversed(lines1):
    print(line.strip())

for line in sorted(lines1):
    print(line.strip())

# ---------------------------------------- The 'For line in file' Technique ----------------------------------------
# When want to do the same thing to every line from the file cursor to the end of a file
# On each iteration, the file cursor is moved to the beginning of the next line
with open('C9_0_0_File_Sample_1.txt') as file4:
    for line in file4:
        print(len(line))  # Each of the lines we read form the file has a newline character at the end, so the
        # length is 1 bigger than expected. We can also use .strip() to get rid of it.
        print(len(line.strip()))

# ---------------------------------------- The readline Technique ----------------------------------------
# When want to read only part of a file; want to treat lines differently depending on context
# Only reads one line at a time
with open('C9_0_1_File_Sample_2') as file5:
    # Read the description line
    file5.readline()

    # Keep reading comment lines until we read the first piece of data
    data = file5.readline().strip()  # Since .readline() only read one line, the .strip() can directly apply on it
    while data.startswith('Source'):
        data = file5.readline().strip()

    # We have the first piece of data;
    # Because we can't read the line again, so when the first data occurs which doesn't satisfy the while condition,
    # we have to receive it by using a variable.
    total_score = int(data)

    # Read the rest of the data
    for rest_data in file5:
        total_score += float(rest_data.strip())

print('Total score is:', total_score)

# If we want to keep indented when printed out, we can use .rstrip() instead of the .strip()
with open('C9_0_1_File_Sample_2') as file6:
    file6.readline()
    data = file6.readline().rstrip()
    while data.startswith('Source'):
        data = file6.readline().rstrip()

    # Because we can't read the line again, so when the first data occurs which doesn't satisfy the while condition,
    # we have to receive it by using a variable.
    print(data)

    for rest_data in file6:
        print(rest_data.rstrip())
