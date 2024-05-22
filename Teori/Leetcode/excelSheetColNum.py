# problem 171 : Excel Sheet Column Number
# Given a string columnTitle that represents the column title as it appears in an Excel sheet, return its corresponding column number.

def titleToNumber(columnTitle):
    """
    Returns the column number corresponding to the given column title.
    """
    # Initialize the column number
    columnNumber = 0

    # Iterate through the characters in the column title
    for char in columnTitle:
        # Convert the character to its corresponding value (A=1, B=2, ..., Z=26)
        value = ord(char) - ord('A') + 1

        # Multiply the current column number by 26 and add the value of the current character
        columnNumber = columnNumber * 26 + value

    return columnNumber # Return the final column number
  
"""Here's how the algorithm works:

    We initialize the column number to 0.
    We iterate through each character in the column title.
    For each character, we calculate its corresponding value by subtracting the ASCII value of 'A' and adding 1.
    We multiply the current column number by 26 and add the value of the current character to get the updated column number.
    After processing all characters, we return the final column number.
    
The time complexity of this algorithm is O(n), where n is the length of the input columnTitle. This is because we iterate through each character in the column title once. The space complexity is O(1), as we are using a constant amount of extra space.
"""

# Test cases
print(titleToNumber("A"))  # Output: 1
print(titleToNumber("AB"))  # Output: 28
print(titleToNumber("ZY"))  # Output: 701
print(titleToNumber("FXSHRXW"))  # Output: 2147483647
print(titleToNumber("AA"))  # Output: 27
print(titleToNumber("BA"))  # Output: 53
print(titleToNumber("ZZ"))  # Output: 702
print(titleToNumber("AAA"))  # Output: 703
print(titleToNumber("ZZZ"))  # Output: 18278