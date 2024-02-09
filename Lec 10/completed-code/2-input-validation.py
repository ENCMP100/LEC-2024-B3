"""
@author: ranaweer
"""

is_non_digit = True
while is_non_digit:
    input_str = input("Enter an integer: ")

    is_non_digit = False
    num_periods_found = 0
    for c in input_str:
        if c == '.':
            num_periods_found = num_periods_found + 1
        
        if not (c>='0' and c <='9' or c == '.' and num_periods_found < 2 and len(input_str) != 1)  :
            is_non_digit = True;
            break # breaking for c in input_str
            
        

print("The number you entered is", float(input_str))


