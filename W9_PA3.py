# Given a square matrix with n rows and n columns, you have to write a program to rotate this
# matrix such that each element is shifted by one place in a clockwise manner.

# For example, given the following matrix
# 1 2 3
# 4 5 6
# 7 8 9

# The output should be
# 4 1 2
# 7 5 3
# 8 9 6

# Input Format:
# The first line of the input contains a number n representing the number of rows and columns.
# After this, there are n rows with each row containing n elements separated by a space

# Output Format:
# Print the elements of the modified matrix with each row in a new line and all the elements
# in each row is separated by a space.

# Example 1:
# Input:
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output:
# 4 1 2
# 7 5 3
# 8 9 6

# Example 2:
# Input:
# 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# Output:
# 5 1 2 3
# 9 10 6 4
# 13 11 7 8
# 14 15 16 12

# Explanation:

# In the first example, there is an odd number of rows and columns hence excluding the
# middle element i.e. 5 all the elements were shifted by one position in a clockwise manner.
# In the second example, there are even number of rows and columns hence all
# the elements were shifted by one position in a clockwise manner.
# --------------------------------------------------------------------------------------------------------

# Take input of size of a matrix.
size = int(input())

# Take elements in a list.
c = size
list = []
list1 = [[int(j) for j in input().split()] for i in range(size)]

for i in list1:
    for j in i:
        list.append(j)

# Define indexing variables as,
# Selected_index, comparing_index.
selected_index = 0
comparing_index = size
temp = 0

# Now start a loop, where selected_index = 0 and comparing index = size of matrix
for i in range(0, len(list)):

    # When index = swapping element. Double the size.
    if selected_index == comparing_index:
        comparing_index = size + comparing_index

    # When comparing index > size of matrix.
    if comparing_index >= len(list):
        comparing_index = len(list) - 2

    # Exceptional case. When index = middle element.
    if len(list)/2 != 0:
        if selected_index == ((len(list)-1) / 2):
            selected_index = selected_index + 1

    # when last element is require to be swapped with second last element.
    if selected_index == (len(list)-1):
        temp = list[(len(list)-1)]
        list[(len(list)-1)] = list[(len(list)-2)]
        list[(len(list)-2)] = temp

    # Swapping of elements.
    if selected_index < comparing_index < len(list)-1:
        temp = list[selected_index]
        list[selected_index] = list[comparing_index]
        list[comparing_index] = temp

    selected_index = selected_index + 1
    print(list)

# For printing the list in matrix way.
for i in range(len(list)):

    if i == size:
        print()
        size = size + c

    if i < size:
        print(list[i], end=" ")


fail - doesn't work as intended.



