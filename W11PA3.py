# Write a program, which will find all such numbers between m and n (both included) such that each digit
# of the number is an even number.

# Input Format:
# The first line contains value m and n separated by a comma.

# Output Format:
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Constraints:
# 1000<=m<=9000
# 1000<=n<=9000 

# -----------------------------------------------------------------------------------------------------------------

# Take input in m and n
m, n = map(int, input().split(sep=","))

# List to store results.
lst = []

for i in range(m,n+1):
    # To check each digit in n either it's even or not.
    s = str(i)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[len(s)-2]) % 2 == 0 and int(s[len(s)-1]) % 2 == 0:
        lst.append(s)

# Printing the required result.
print(*lst, sep=",", end="")
