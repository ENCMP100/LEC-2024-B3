"""
Created on Wed Jan 22 20:32:47 2024

@author: ranaweer
"""


# Boolean variables hold boolean values (True or False)

x = True
y = False

a = 20 <= 80
b = 20 <= 10

# Boolean operators:
# ==================

# and operator
# Produces True if ALL conditions are True

25 < 0  and 25 < 10 # False, since the first condition is False
                    # The second condition is also False but it will
                    # not even be evaluated since the first one is False

25 < 0  and 25 < 100 # False, again since the first condition is False

25 < 50  and 25 < 10 # False, since the second condition is False 
25 < 50  and 25 < 100 # True, since BOTH conditions are True 


# or operator
# Produces True as long as at least one condion is True

25 < 0  or 25 < 10 # False, since BOTH conditions are False

25 < 0  or 25 < 100 # True, since the second condition is True

25 < 50  or 25 < 10 # True, since the first condition is True
                    # The second condition is not even evaluated
                    # since the first condition is True

25 < 50  or 25 < 100 # True, since the first condition is True
                     # The second condition is also true but it
                     # is not even evaluated since the first 
                     # condition is already True



# not operator
# Negates the result of a condition

not 10 < 100 # False, since the condition is True

not 1000 < 100 # True, since the condition is False


# Operator Precedence
# ===================

# Relational operators have higher precedence than
# Boolean operators. Therefore, relational operators
# are evaluated first and their results are combined
# using Boolean operators

25 < 0  and 25 < 100
(25 < 0)  and (25 < 100) # This is same as the above 


# All Boolean operators have the same precedence, 
# so they are evaluated from left to right unless
# we group them by parantheses

not 25 < 0  and 25 < 10
# Evaluation of the above expression is as follows
# First evaluates the relational operations, 
# becaude they have higher precedence than Boolean operartors
# This results in the following
#
#        not False and False
#
# Now, since there are no grouping by parantheses,
# the first Boolean operator is applied to the next
# part of the expression, i.e. not False, which
# results in True. Hence the expression is simplified
# as follows
#
#       True and False
#
# And the above produces a final result of False

# If you want to negate the result of the "and" operation,
# then you should use parantheses as follows.
  
not 25 < 0  and 25 < 10
not(25 < 0  and 25 < 10)








