##
#  This program prints the average of salary values that are terminated with 
#  a sentinel.
#

# Initialize variables to maintain the running total and count.
total = 0.0
count = 0

# Initialize salary to a non-sentinel value.
salary = 0.0

# Process data until the sentinel is entered.
print("Please input salary. Enter a negative number to finish the input intake.")
while salary >= 0.0 :
   salary = float(input("Salary: "))
   if salary >= 0.0 :
      total = total + salary
      count = count + 1
   
# Compute and print the average salary.
if count > 0 :
   average = total / count
   print("Average salary is", average)
else :
   print("No data was entered.")

