# Given a list of numbers (integers), find second maximum and second minimum in this list.

# Input Format:
# The first line contains numbers separated by a space.

# Output Format:
# Print second maximum and second minimum separated by a space

# Example:
# Input:
# 1 2 3 4 5

# Output:
# 4 2

# -----------------------------------------------------------------------------------------------------------------

NumList = list(map(int, input().strip().split()))[:]

first = second = NumList[0]

for j in range(len(NumList)):

    # For second maximum:
    if NumList[j] > first:
        second = first
        first = NumList[j]
    else:
        if (NumList[j] > second) and (NumList[j] < first):
            second = NumList[j]

print(second, end=" ")


for j in range(len(NumList)):

    # For second minimum:
    if NumList[j] < first:
        second = first
        first = NumList[j]
    else:
        if (NumList[j] < second) and (NumList[j] != first):
            second = NumList[j]

print(second, end="")