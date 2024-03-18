## Reading records
#
#  Usually, a text data file may contain multiple records of data.
#  A record of data may represent multiple data fields presented
#  in one line.
#  For example, in temp-1.csv, the 2nd (index 1) value and the 
#  5th value (index 4) in row 2 onwards represent the date 
#  and the average daily temperature. We will need to process
#  the line (split by comma) to extract these values.
#
#  E.g. The following code caluclates the average temperature
#  over the total period

file = open("temp-1.csv", "r")

numDays = 0
sumOfTemp = 0
isFirstline = True
for line in file:
    if isFirstline:
        # Skip the first line since it is the header
        isFirstline = False
        continue # skip the rest and go to the next iteration
                 # of the FOR loop
                 
    #Processing the record
    parts = line.split(',')
    date = parts[1]
    temp = float(parts[4])
    
    sumOfTemp = sumOfTemp + temp
    numDays = numDays + 1
    
averageTemperture = sumOfTemp/numDays
print("Average temperature over %d days = %.2f" % (numDays, averageTemperture))
