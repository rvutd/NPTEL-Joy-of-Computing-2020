# Write a Python program to get a string made of the first 2 and the last 2 chars from a
# given a string. If the string length is less than 2, return instead of the empty string.

# Input Format:
# The first line of the input contains the String S.

# Output Format:
# The first line of the output contains the modified string.

# Sample Input:
# Programming

# Sample Output:
# Prng

word = input()


# function to print First two and last two letters of of a word.
def First_Last(word):

    # Empty string variable to store words required.
    FL = ""

    for i in range(0, len(word)):

        # for each letter in word. e_ch is each character in word.
        e_ch = word[i]

        # To Check if word length is less than 2. Therefore Print Null.
        if len(word) < 2:
            break

        # To Check if i (letter) 1st two and last two. Therefore Print Null
        else:
            if i <= 1 or i >= (len(word) - 2):
                FL = FL + e_ch

    return FL


print(First_Last(word))
