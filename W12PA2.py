# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Input Format:
# The first line of the input contains a statement.

# Output Format:
# Print the number of upper case and lower case respectively separated by a space.

# Example:

# Input:
# Hello world!

# Output:
# 1 9

# ----------------------------------------------------------------------------------------------------------------

def upper_lower_case_count(string):

    count_upper = 0
    count_lower = 0
    
    for i in range(len(string)):
        if string[i].islower() == True:
            count_lower += 1

        if string[i].isupper() == True:
            count_upper += 1
        
        if string[i].isspace() == True:
            continue
        
        else:
            continue
        
    return print(count_upper, count_lower, end="")


string = input()
upper_lower_case_count(string)


