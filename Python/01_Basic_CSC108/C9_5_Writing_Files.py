"""
1) replace 'w' from 'r' in open()
    a) If the filename has already existed, the file contents are erased and replaced;
    b) If the filename doesn't exist already, then a new file is created.
    c) In addition to writing characters o file, method write returns the number of characters written.
2) replace 'a' from 'r' in open()
    a) The data we write is added to the end of the file and the current file contents are not overwritten.
3) method write() doesn't automatically start a new line; if you want to end in a newline, you have to include '\n'
"""
with open('C9_0_1_File_Sample_2', 'w') as output_file:
    output_file.write('Computer Science')  # returns 16

with open('C9_0_1_File_Sample_2', 'a') as output_file:
    output_file.write('Software')

with open('C9_0_1_File_Sample_2') as read:
    print(read.read())

with open('C9_0_2_File_Sample_3', 'a') as output_file:
    output_file.write('Software\n')
    output_file.write('Engineer\n')

with open('C9_0_2_File_Sample_3') as read2:
    print(read2.read())


def sum_number_pairs(input_file, output_filename: str) -> None:
    """
    :param input_file: Contains two floats per line separated by a space
    :param output_filename: for each line in input_file, write a line to the output file that contains the two floats
     from the corresponding line of input_file plus a space and the dum of the two floats
    """
    with open(output_filename, 'w') as data_output:
        for number_pair in input_file:
            number_pair = number_pair.strip()
            operands = number_pair.split()
            total = float(operands[0]) + float(operands[1])
            new_line = '{0} {1}\n'.format(number_pair, total)
            data_output.write(new_line)


sum_number_pairs(open('C9_0_3_File_Sample_4'), 'C9_0_4_File_Sample_5')

with open('C9_0_4_File_Sample_5') as read3:
    print(read3.read())
