# Write a program that accepts a comma-separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically.

# Input Format:
# The first line of input contains words separated by the comma.

# Output Format:
# Print the sorted words separated by the comma.

# Example:

# Input:
# without,hello,bag,world

# Output:
# bag,hello,without,world 

# -----------------------------------------------------------------------------------------------------------------

# Take input in list.
string = list(map(str, input().split(sep=",")))[:]

# Sort list in alphabetic order as it's string.
string = sorted(string)

# Printing the required result.
print(*string, sep=",", end="")
