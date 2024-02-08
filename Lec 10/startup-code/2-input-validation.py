"""
@author: ranaweer
"""

is_non_digit = True
while is_non_digit:
    input_str = input("Enter an integer: ")

    is_non_digit = False
    for c in input_str:
        if not (c>='0' and c <='9'):
            is_non_digit = True;
            break # breaking for c in input_str

print("The number you entered is", int(input_str))


