# Given a list A of elements of length N, ranging from 1 to N. 
# All elements may not be present in the array.
# If the element is not present then there will be -1 present in the array. 
# Rearrange the array such that A[i] = i and if i is not present display -1 at that place.

# Input Format:
# The first line contains n numbers with each number separated by a space.

# Output Format:
# Print the elements of the list after the modification.

# Example:
# Input:
# -1 -1 6 1 9 3 2 -1 4 -1

# Output:
# -1 1 2 3 4 -1 6 -1 -1 9

# Explanation:
# The modified list contains elements such that A[i] = i

# --------------------------------------------------------------------------------------------

# Take input in list.
lst = list(map(int, input().split()))[:]

# Sort the list so all -1 are in begining.
# Note that Number of -1 in list = number of missing elements.
lst.sort()

# For swapping.
temp = 0

# i is basicallly the number starting from 0.(whole numbers)
for i in range(0, len(lst)):
    # If i = j(any other elements in list) then swap.
    for j in range(0, len(lst)):

        if i == lst[j]:
            # Swapping.
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

# Printing the required output.
for i in range(0, len(lst)):
    if i < (len(lst)-1):
        print(lst[i], end=" ")
    if i == (len(lst)-1):
        print(lst[i], end="")
    if (len(lst)) == 0:
        print("-1", end="")


# Sort the list in such a way that all -1 in list are at last.
# And all +ve number are from 0 to n (increasing order).

# def count_element(lst):
    
#     count = 0

#     for i in range(0, len(lst)):
#         if lst[i] == -1:
#             count += 1

#     return count


# res = count_element(lst)
# print(res)

# def suffix_element(list):

#     j = len(lst) - 1
#     temp = 0
#     lst.sort()

#     for i in range(0, len(list)):
        
#         if list[i] == -1 and i < j:
#             print(i)
#             temp   = lst[i] 
#             lst[i] = lst[j]
#             lst[j] = temp

#             j = j - 1

#     return lst

# print(suffix_element(lst))


