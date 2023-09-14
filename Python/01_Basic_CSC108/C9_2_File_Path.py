"""
1) Python assumes that the file you want to read is in the same directory as the program that is doing the reading
(in the same folder)
2) File Path: specifies a location in your computer's file system
    a) Absolute Path: contains the sequence of directories to a file, starting at the root directory ar the top of the
    file system, and optionally includes the name of a file
        § Both Apple OSX and Linux use a forward slash as the directory separator
            e.g. /Users/henryw/Desktop/UOT/Courses/CSC/CSC108/Python_Notes/C9_2_File_Path.py
        § Windows begins with a drive letter, such as C; and used a backslash as the directory separator( will be auto-
        -matically translate to work in Windows.
            e.g. 'C:\Users\henryw\Desktop\UOT\Courses\CSC\CSC108\Python_Notes\C9_2_File_Path.py'
    b) Relative Path: relative to the current working directory.
        § change Python's working directory to a different directory using function chdir
3) Current Working Directory: the directory in which Python looks for files. When running a Python program, the current
 working directory is the directory where that program is saved
 e.g. if the path of the file is saved in: /Users/henryw/Desktop/UOT/Courses/CSC/CSC108/Python_Notes/C9_2_File_Path.py
      Then, the current working directory is /Users/henryw/Desktop/UOT/Courses/CSC/CSC108/Python_Notes
"""
# ---------------------------------------- Absolute Path ----------------------------------------
import os

os.getcwd()

# ---------------------------------------- Relative Path ----------------------------------------
os.chdir('Users/henryw/Desktop')
os.getcwd()

# Suppose a program called reader.py and a directory called data in the same directory as reader.py.
# Inside a data have files called data1.txt and data2.txt
# Opening the data1.txt by using relative path shows:
open('date/data1.txt', 'r')

# To look in the directory above the current working directory, using two dots:
open('../data1.txt', 'r')

# Can chain them to go up multiple directories
# looks for data1.txt three directories above the current working directory and then down into a data directory
open('../../../data/data1.txt', 'r')
