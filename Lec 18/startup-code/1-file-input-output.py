## Input / Output Opetations with Text Files
#

## READLINE: reading from a Text File
#  ========================

# To read data from a file, we should first open the file in "READ" mode
infile = open("temp-1.csv", "r")

# We cab read this file one line at a time until the end
line = infile.readline()
while line != "":
    print(line, end="") 
    line = infile.readline()

# The file must be closed after reading
infile.close()


# Instead of reading line by one using the readline function,
# Python allows us to iterate though lines in the opened file
# using a FOR loop. In this case, the opened file behaves like
# a container of strings, where each line is a string in the container
infile = open("temp-1.csv", "r")

for line in infile:
    print(line)

infile.close()


## READ: reading a file one (or more) characters at a time
#  =======================================================

import time # to use time.sleep function to add some delay 
            # for demonstration purposes

file = open('mary.txt')

char  = file.read(1) # Read one character
while char != "":
    print(char, end="")
    time.sleep(0.2) # Just wait for 0.2 second before continuing 
                    # so that we can see the character-by-character
                    # printing. 
                    # time.sleep is NOT IN EXAM SYLLABUS
    char  = file.read(1)

file.close()

## Writing to a Text File
#  ======================

# To write to a text file, you should open thr file in the "WRITE" mode
outfile = open("hello.txt", "w")

outfile.write('Hello World!\n')
outfile.write('How are you?\n')
outfile.write('It\'s a nice day\n')

# The file must be closed after writing
outfile.close()


# We can also use print to write to a file
outfile = open("print-out.txt", "w")
print('Hello World!', file=outfile)
print('How are you?', file=outfile)
print('It\'s a nice day', file=outfile)
outfile.close()
