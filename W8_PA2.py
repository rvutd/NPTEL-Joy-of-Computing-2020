# A panagram is a sentence containing every 26 letters in the English alphabet.
# Given a string S, check if it is panagram or not.

# Input Format:
# The first line contains the sentence S.

# Output Format:
# Print 'YES' or 'NO' accordingly

# Example:
# Input:
# The quick brown fox jumps over the lazy dog

# Output:
# YES
import string


def ispangram(str1, alphabet=string.ascii_lowercase):

    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


if ispangram(input()):
    print("YES", end="")
else:
    print("NO", end="")
