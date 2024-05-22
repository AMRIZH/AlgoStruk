# problem 326 : Power of Three
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.

def isPowerOfThree(n):
    """
    Returns True if n is a power of three, False otherwise.
    """
    # Check if n is positive
    if n <= 0:
        return False
    
    # Check if n is a power of three
    return 1162261467 % n == 0 # 1162261467 is the largest power of three that fits in 32-bit signed integer
  
"""Here's how the algorithm works:

    We first check if the input integer n is positive. If n is not positive, it cannot be a power of three, so we return False.
    We then check if n is a power of three by checking if 1162261467 is divisible by n. 1162261467 is the largest power of three that fits in a 32-bit signed integer.
    If n is a power of three, the function returns True. Otherwise, it returns False.
    
    The time complexity of this algorithm is O(1), as it performs constant-time operations on the input integer n. The space complexity is also O(1), as the algorithm uses a fixed amount of memory."""
    
# Test cases
print(isPowerOfThree(27))  # Output: True
print(isPowerOfThree(9))  # Output: True
print(isPowerOfThree(45))  # Output: False
print(isPowerOfThree(0))  # Output: False
print(isPowerOfThree(-27))  # Output: False
print(isPowerOfThree(81))  # Output: True
print(isPowerOfThree(243))  # Output: True