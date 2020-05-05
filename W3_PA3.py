# Given a list A of numbers (integers), you have to print those numbers which are not multiples of 5.

# Input Format:
# The first line contains the numbers of list A separated by a space.

# Output Format:
# Print the numbers in a single line separated by a space which are not multiples of 5.

# Example:
# Input:
# 1 2 3 4 5 6 5

# Output:
# 1 2 3 4 6

# Explanation:
# Here the elements of A are 1,2,3,4,5,6,5 and since 5 is the multiple of 5,
# after removing them the list becomes 1,2,3,4,6
# --------------------------------------------------------------------------------------------------------------

num = list(map(int, input().strip().split()))[:]
yup = []

for j in range(len(num)):
    if (num[j] % 5) != 0:
       yup.append(num[j])

i = len(yup) - 1
for j in range(len(yup)):
    if j < i:
        print(yup[j], end=" ")
    else:
        print(yup[j], end="")