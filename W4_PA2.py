# Given an integer number n, you have to print the factorial of this number.
# To know about factorial please click on this link.

# Input Format:
# A number n.

# Output Format:
# Print the factorial of n.

# Example:
# Input:
# 4

# Output:
# 24

num = int(input())

factorial = int(1)

for i in range(num):
    factorial = factorial * num
    num = num - 1

print(factorial, end="")