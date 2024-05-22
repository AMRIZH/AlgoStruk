# problem 258 : Add Digits
# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

def addDigits(num):
    """
    Returns the result of repeatedly adding all the digits of a given number until it has only one digit.
    """
    # Handle edge case where num is 0
    if num == 0:
        return 0

    # Calculate the digital root of the number
    return 1 + (num - 1) % 9
  
"""Here's how the algorithm works:

    We handle the edge case where the input number num is 0 by returning 0.
    We calculate the digital root of the number using the formula 1 + (num - 1) % 9.
    The digital root of a number is the result of repeatedly adding all its digits until it has only one digit. The formula above calculates the digital root in constant time.
    
The time complexity of this algorithm is O(1), as it performs a fixed number of operations regardless of the input number. The space complexity is also O(1), as the algorithm uses a constant amount of extra space.
"""

# Test cases
print(addDigits(38))  # Output: 2
print(addDigits(0))  # Output: 0
print(addDigits(9))  # Output: 9
print(addDigits(12345))  # Output: 6
print(addDigits(999))  # Output: 9
print(addDigits(123456789))  # Output: 9
print(addDigits(987654321))  # Output: 9
print(addDigits(1234567890))  # Output: 9
print(addDigits(9876543210))  # Output: 9
print(addDigits(12345678900))  # Output: 9

