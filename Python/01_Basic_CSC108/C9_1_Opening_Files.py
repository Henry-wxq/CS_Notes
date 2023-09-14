"""
1) A file cursor: the marker that keeps track of the current location in the file(acts as a bookmark)
    a) the file cursor is initially at the beginning of the file, but as we read or write data, it moves to the end
    of what we just read or wrote
"""
# ---------------------------------------- Method 1: Built-in Function: open() ----------------------------------------
# open(file, mode): opens a file and returns an object that knows how to get information form the file, how much
# you've read, and which part of the file you're about to read next.
# file: the name of the file to open
# mode: the file mode: 'r' for read; 'w' for write; 'a' for appending;
# if call open with only the name of the file, then the default is 'r'
file = open('C9_0_0_File_Sample_1.txt')

# .read(): Tells Python to read the contents of the entire file into a string(More different Techniques in C9_2)
contents = file.read()

# The newline characters are treated like every other characters; a newline character is just another character in(but
# it won't be printed out explicitly
# the file
print(contents)

# .close(): releases all resources associated with the open file object
# every call on function open() should have a corresponding call on method .close()
file.close()

# ---------------------------------------- Method 2: with Statement ----------------------------------------
'''
general form of with Statement:
    with open(<<filename>>, <<mode>>) as <<variable>>:
        <<block>>
'''
# automatically close a file when the end of the block is reached
with open('C9_0_0_File_Sample_1.txt', 'r') as file:
    contents = file.read()

print(contents)
