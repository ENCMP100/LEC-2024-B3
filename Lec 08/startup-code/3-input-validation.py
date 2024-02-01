#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:41:29 2023

@author: ranaweer
"""
# If a program takes user input, we should validate these inputs before
# we process them. This is because the user can input an invalid input

# E.g. the following code from Hortsman 3.9

##
#  This program simulates an elevator panel that skips the 13th floor, 
#  checking for input errors.
#

# Obtain the floor number from the user as an integer.
floor = int(input("Floor: "))
   
# Make sure the user input is valid.
if floor == 13 :
   print("Error: There is no thirteenth floor.")
elif floor <= 0 or floor > 20 :
   print("Error: The floor must be between 1 and 20.")    
else :    
   # Now we know that the input is valid
   actualFloor = floor
   if floor > 13 :
      actualFloor = floor - 1
      
   print("The elevator will travel to the actual floor", actualFloor)

