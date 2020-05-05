# Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalised.

# Input Format:
# The first line of the input contains a number n which represents the number of line.
# From second line there are statements which has to be converted. Each statement comes in a new line.

# Output Format:
# Print statements with each word in capital letters.

# Example:

# Input:
# 2
# Hello world
# Practice makes perfect

# Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# ----------------------------------------------------------------------------------------------------------------

# Number of lines.
nol = int(input())

# To put require result in list.
lines = []

# To get line input.
for i in range(nol):

    # Line by line input in a string.
    s = input()

    # If s has input in it then. Append to list by updating 
    # each element to upper case.
    if s:
        lines.append(s.upper())
    

# Printing the required output.
for i in range(len(lines)):

    if i == len(lines)-1:
        print (lines[i], end="")
    else:
        print (lines[i])


