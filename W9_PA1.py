# Given a string, you need to convert all lowercase letters to uppercase letters
# and vice versa.

# Input Format:
# A single line containing a string S.

# Output Format:
# Print the modified string S.

# Sample Input:
# Hello World!!

# Sample Output:
# hELLO wORLD!!

String = input()


# Function to swap cases.
def swap_case(String):

    # Empty String to store changed cases.
    swap_word = ""

    # To check each letter in word.
    for i in range(0, len(String)):

        # Taking one character of string at a time.
        character = String[i]

        # Checking if character is small.
        if character.islower() == True:
            character = character.upper()
            swap_word = swap_word + character

        # Checking if character is big alphabet.
        elif character.isupper() == True:
            character = character.lower()
            swap_word = swap_word + character

        # Checking if character is special of anything else.
        else:
            swap_word = swap_word + character

    return swap_word


print(swap_case(String), end="")

