## CSV Reader
#  ==========
#
# Python has dedicated data-file readers to help us read data from standard
# formats. CSV Reader is one of such readers designed to help reading data
# from Comma Separated Value format


from csv import reader
#import csv as reader # Anotehr way to import csv reader. 
                      # If you do this, you will need to create 
                      # the reader as csvReader = reader.reader(file)

## READ: reading a file cone of more characters at a time
#

file = open('temp-2.csv', 'r') 

# The above file contains complex CSV records where some fields (e.g. last
# field in some records) contains commas within those values. We should not
# split those fields with commas. Therefore, processing such records is more
# complex than simply splitting each line by commas.
# CSV Reader object is very helpful in reading such complex CSV files.

csvReader = reader(file)
for row in csvReader: # Returns each record row as a list of values.
    print(row)

file.close() # Close the file afer reading


## NEXT: skips a line in a CSV reader.
#        Useful, for example, to skip a header row.
file = open('temp-2.csv', 'r') 
csvReader = reader(file)
next(csvReader) # Skips the first row, which is the header

for row in csvReader:
    print(row)
file.close() # Close the file afer reading



## CSV Writer
# 
# CSV Writer allows you to write lists to Comma Separated Value (CSV)  files
#
# E.g.

from csv import writer

file = open('csv-output.csv', 'w')

csvWriter = writer(file)

csvWriter.writerow(["Name", "Id", "Class", "Average"])
csvWriter.writerow(["John Smith", 1607, "Senior", 3.28])
csvWriter.writerow(["Jimmy Fernando", 2431, "Junior", 3.64])
csvWriter.writerow([]) # Writing an empty row, just to show the possibility
csvWriter.writerow(["Aiyana Jacob", 3261, "Junior", 2.78])

file.close()