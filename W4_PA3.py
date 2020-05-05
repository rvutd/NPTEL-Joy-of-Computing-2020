# You are provided with the number of rows (R) and columns (C).
# Your task is to generate the matrix having R rows and C
# columns such that all the numbers are in increasing order starting from 1 in row wise manner.

# Input Format:
# The first line contain two numbers R and C separated by a space.

# Output Format:
# Print the elements of the matrix with each row in a new line and elements of each row are separated by a space.

# NOTE: There should not be any space after the last element of each row and no new line after the last row.

# Example:
# Input:
# 3 3

# Output:
# 1 2 3
# 4 5 6
# 7 8 9

# Explanation:
# Starting from the first row, the numbers are present in the increasing order.
# Since it's a 3X3 matrix, the numbers are from 1 to 9

R, C = map(int, input().split())
num = int(1)
ln = R * C

for j in range(C):
    for i in range(R):
        if num % C != 0:
            print(num, end=" ")
            num = num + 1
        else:
            if num != ln:
                print(num)
                num = num + 1
            else:
                print(num, end="")
