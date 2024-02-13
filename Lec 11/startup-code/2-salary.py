"""
  This program prints the average of salary values that are terminated with 
  a sentinel.
  Reference: Python Programming for Engineers of University of Alberta
             by Cay S Hortsmann
"""

#  How can we use data in a text file (salary-data.txt) to calculate the 
#  average salary instead of having to enter them manually every time?

# Initialize variables to maintain the running total and count.
total = 0
count = 0

# Initialize salary to any non-sentinel value.
salary = 0
sentinel = -1

# Read data and calculate the total until the sentinel is entered.
while True :
   salary = int(input())
   if salary == sentinel :
       break

   total = total + salary
   count = count + 1
   
# Compute and print the average salary.
if count > 0 :
   average = total / count
   print("Average salary is", average)
else :
   print("No data was entered.")

