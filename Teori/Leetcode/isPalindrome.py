# problem 125 : Valid Palindrome
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def isPalindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string is a palindrome
    return s == s[::-1]

"""Here's how the code works:

    The first line s = ''.join(char.lower() for char in s if char.isalnum()) cleans the input string s by:
        Converting all characters to lowercase using char.lower()
        Keeping only alphanumeric characters using char.isalnum()
        Joining the remaining characters into a new string
    After cleaning the string, we check if it is equal to its reverse using s == s[::-1]. The expression s[::-1] creates a new string that is the reverse of s.
    The function returns True if the cleaned string is equal to its reverse (i.e., it's a palindrome), and False otherwise.

The time complexity of this solution is O(n), where n is the length of the input string s, because we need to iterate through the string once to clean it and check if it is equal to its reverse. The space complexity is O(n) as well, since we create a new string during the cleaning process.
"""

# test the function
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # Output: True

s = "race a car"
print(isPalindrome(s))  # Output: False

s = " "
print(isPalindrome(s))  # Output: True