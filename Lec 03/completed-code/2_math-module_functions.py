"""
Run the program and review values in the Variable Explorer in Spyder

@author: ranaweer
"""


from math import sqrt, trunc, radians, degrees, sin, cos, tan, exp, log, pi

# Square Root of a number
x1 = 25
square_root_value = sqrt(x1)

# Round off error
# Calculate and print the square of the square-root of 2
sqrt_2 = sqrt(2)
square_sqrt_2 = sqrt_2 * sqrt_2


# Use exponential operator and square root function to caluclate
# hypotenuse of a right-angle triangle
a = 4
b = 3
hypotenuse = sqrt(a**2 + b**2)

# Truncate a floating point number to an integer
x2 = 7.75
truncated_value = trunc(x2)


# Converting degrees to radians
myDeg = 30
radian_value = radians(myDeg)

# Converting radians to degrees
myRad = pi/4
degree_value = degrees(myRad)

# sin, cos, and tan values of 30 degrees
angleInDegrees = 30

deg_val = radians(angleInDegrees)
sin_value = sin(deg_val)
cos_value = cos(deg_val)
tan_value = tan(deg_val)


# Exponent to the euler number or the base of natural logerithm (e.g. e to-the x)
n = 3
e_to_the_3 = exp(n)

# Logarithm
natural_log_of_20 = log(20)

base_10_log_of_1000 = log(1000, 10)

