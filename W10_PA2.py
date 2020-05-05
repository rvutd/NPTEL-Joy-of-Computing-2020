# Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates. 

# Input Format:
# The first line contains n-1 numbers with each number separated by a space.

# Output Format:
# Print the missing number

# Example:

# Input:
# 1 2 4 6 3 7 8

# Output:
# 5

# Explanation:
# In the above list of numbers 5 is missing and hence 5 is the input.

# ------------------------------------------------------------------------------------------------------

# Take input in a list.
list = list(map(int, input().split()))[:]

# As starting integers are from 1 (Given). Let's
num = 1
i = 0

while i < len(list):
    # To check if number is in list or not. If not 
    # then it's the missing number.
    if num not in list:
        missing_num = num 
	
    # As range of integers in list btw 1 to n.
    # increment n by 1.
    num += 1
    i += 1
    
print(missing_num, end="")
