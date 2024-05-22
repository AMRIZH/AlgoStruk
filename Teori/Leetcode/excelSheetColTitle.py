# problem 168 : Excel Sheet Column Title
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Create a list of characters for mapping
        mapping = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        
        # Initialize an empty string to store the column title
        title = ""
        
        while columnNumber:
            # Subtract 1 from columnNumber to handle the base-26 indexing
            columnNumber -= 1
            
            # Get the remainder by taking modulus with 26
            remainder = columnNumber % 26
            
            # Append the corresponding letter to the title string
            title = mapping[remainder] + title
            
            # Update columnNumber by integer division with 26
            columnNumber //= 26
        
        return title

"""Here's how the algorithm works:

    We create a list mapping that maps the indices to the corresponding letters of the alphabet.
    We initialize an empty string title to store the column title.
    We enter a loop that continues until columnNumber becomes 0.
    Inside the loop, we first subtract 1 from columnNumber to handle the base-26 indexing (since 'A' represents 1, not 0).
    We get the remainder by taking the modulus of columnNumber with 26. This remainder gives us the index of the corresponding letter in the mapping list.
    We append the letter at the index remainder to the beginning of the title string.
    We update columnNumber by performing integer division with 26, which gives us the next digit in the base-26 number.
    After the loop ends, we return the title string.


The time complexity of this algorithm is O(log(columnNumber)), where columnNumber is the input integer. This is because we are dividing the columnNumber by 26 in each iteration of the loop. The space complexity is O(log(columnNumber)) as well, as the length of the title string is proportional to the number of iterations in the loop.
"""