# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the company name of a given email address. 
# Both user names and company names are composed of letters only.

# Input Format:
# The first line of the input contains an email address.

# Output Format:
# Print the company name in single line.

# Example;

# Input:
# john@google.com

# Output:
# google 

# -------------------------------------------------------------------------------------------------------

# Take input in string.
string = input()

# Empty string to store name of company.
empty = ""

# To run loop till last letter or email.
for i in range(len(string)):
    
    # To check if character in string is @. 
    if string[i] == "@":
      	# j is elements after @ are name of the company.
        j = i + 1 
        # Loop - until elements befor "." are name of the company.
        while string[i] != ".":
          	# To stop loop when element at j position is "."
            if string[j] == ".":
                break
            # To store required result.
            empty = empty + string[j]
			# incrementation.
            j += 1
    
# Printing the required result.
print(empty, end="")

