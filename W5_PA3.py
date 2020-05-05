# A semiprime number is an integer which can be expressed as a product of two distinct primes.
# For example 15 = 3*5 is a semiprime number but 9 = 3*3 is not .
# Given an integer number N,
# find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct).

# Input Format:
# The first line contains an integer N.

# Output Format:
# Print 'Yes' if it is possible to represent N as a sum of two semiprimes 'No' otherwise.

# Example:
# Input:
# 30

# Output:
# Yes

# Explanation:
# N = 30 can be expressed as 15+15 where 15 is a semi-prime number (5*3 = 15)

# NOTE: N is less than equal to 200

num = int(input())
div = num / 2
i: int = 2

# To check if it is integer or not.
if div == int(div):
    print("yes")
    # To Check if it is prime number or not
    while i <= div:
    
        if i < div and div % i == 0:
            break
    
        elif div % i == 0 and i == div:
            print(div)
    
        i += 1
else:
    print("No")
