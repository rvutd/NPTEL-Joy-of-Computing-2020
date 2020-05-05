# You all have seen how to write loops in python. Now is the time to implement what you have learned.

# Given an array A of N numbers (integers), you have to write a program which prints the sum of the
# elements of array A with the corresponding elements of the reverse of array A. If array A has
# elements [1,2,3], then reverse of the array A will be [3,2,1] and the resultant array should be [4,4,4].


# Input Format:
# The first line of the input contains a number N representing the number of elements in array A.
# The second line of the input contains N numbers separated by a space. (after the last elements, there is no space)


# Output Format:
# Print the resultant array elements separated by a space. (no space after the last element)

# Example:
# Input:
# 4
# 2 5 3 1

# Output:
# 3 8 8 3

# Explanation:
# Here array A is [2,5,3,1] and reverse of this array is [1,3,5,2] and hence the resultant array is [3,8,8,3]

# -------------------------------------------------------------------------------------------------------------

# taking number of elements to be stored.

b = int(input())
lis = list(map(int, input().strip().split()))[:b]

# reversing the list of elements and storing in variable rev.
rev = []
rev = lis

rev.reverse()

# adding reverse list and given list
add = []
j = b - 1

for i in range(b):
    add.append(lis[i] + rev[j])
    j = j - 1

# printing sum of two lists.
j = b - 1
for i in range(b):
    if i < j:
        print(add[i], "", end="")
    else:
        print(add[i], end="")