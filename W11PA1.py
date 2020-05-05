# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.

# Input Format:
# A sequence of values for D with each value separated by a comma.

# Output Format:
# Print the sequence of Q values with each value separated by a comma.

# Example:

# Input:
# 100,150,180

# Output:
# 18,22,24

import math

# Taking Input
D = list(map(int, input().split(sep=",")))[:]

# Constants
C = 50
H = 30 

# Empty list to put result in it.
Q = []

for i in range(len(D)):
    # Given Operation one each values.
    seq = (math.sqrt( ( 2 * C * D[i] ) / H ))
    # Rounding to the mathematical values as required result is integer.
    seq = round(seq)
    # Assigning value in Q list.
    Q.append(seq)    


# Printing the required result.
print(*Q,sep=",",end="")

