

# Reading text file line by line (method 1)
infile = open('mary.txt', 'r')
line = infile.readline()
while line != "":
    print(line, end="") 
    line = infile.readline()
infile.close()

# Reading text file line by line (method 2)
infile = open('mary.txt', 'r')
for line in infile:
    print(line, end="")
infile.close()


# Writing to a text file (method 1)
outfile = open("hello.txt", "w")
outfile.write('Hello World!\n')
outfile.write('How are you?\n')
outfile.write('It\'s a nice day\n')
# The file must be closed after writing
outfile.close()

# Writing to a text file (method 2)
outfile = open("print-out.txt", "w")
print('Hello World!', file=outfile)
print('How are you?', file=outfile)
print('It\'s a nice day', file=outfile)
outfile.close()


# Reading from a CSV (comma-separated-value) file
from csv import reader
file = open('temp-2.csv', 'r') 
csvReader = reader(file)
for row in csvReader: # Returns each record row as a list of values.
    print(row)
file.close() # Close the file afer reading

# Writing to a CSV file (method 1)
from csv import writer
file = open('csv-output.csv', 'w')
csvWriter = writer(file)
csvWriter.writerow(["Name", "Id", "Class", "Average"])
csvWriter.writerow(["John Smith", 1607, "Senior", 3.28])
csvWriter.writerow(["Jimmy, Fernando", 2431, "Junior", 3.64])
csvWriter.writerow([]) # Writing an empty row, just to show the possibility
csvWriter.writerow(["Aiyana Jacob", 3261, "Junior", 2.78])
file.close()
