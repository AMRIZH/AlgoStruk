# problem 231 : Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

def isPowerOfTwo(n):
    """
    Returns True if n is a power of two, False otherwise.
    """
    # Check if n is positive
    if n <= 0:
        return False
    
    # Check if n is a power of two
    return n & (n - 1) == 0 # n & (n - 1) clears the least significant bit of n
  
"""Here's how the algorithm works:

    We first check if the input integer n is positive. If n is not positive, it cannot be a power of two, so we return False.
    We then check if n is a power of two by using the bitwise AND operation n & (n - 1). If n is a power of two, n & (n - 1) will clear the least significant bit of n, resulting in 0.
    If n is a power of two, the function returns True. Otherwise, it returns False.
    
    The time complexity of this algorithm is O(1), as it performs constant-time operations on the input integer n. The space complexity is also O(1), as the algorithm uses a fixed amount of memory."""
    
# Test cases
print(isPowerOfTwo(1))  # Output: True
print(isPowerOfTwo(16))  # Output: True
print(isPowerOfTwo(218))  # Output: False
print(isPowerOfTwo(0))  # Output: False
print(isPowerOfTwo(-16))  # Output: False
print(isPowerOfTwo(1024))  # Output: True
print(isPowerOfTwo(1023))  # Output: False
print(isPowerOfTwo(64))  # Output: True

"""
The bitwise AND operation (&) is a binary operation that takes two equal-length binary representations and performs the logical AND operation on each pair of the corresponding bits. In simpler terms, it compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the result bit is set to 0.

The expression n & (n - 1) is a common bit manipulation trick. For numbers that are powers of two, their binary representation has a single bit set to 1 (the bit in the position that corresponds to the power of two), and all other bits are set to 0. When you subtract 1 from this number, all the bits lower than the bit set to 1 flip to 1, and the bit set to 1 flips to 0. So, when you perform a bitwise AND operation on the original number and the decremented number, the result will be 0.

For example, let's take the number 8, which is a power of two. In binary, 8 is represented as 1000. If we subtract 1 from 8, we get 7, which in binary is 0111. If we perform a bitwise AND operation on 1000 (8) and 0111 (7), the result is 0000 (0).

The return n & (n - 1) == 0 statement returns True if n is a power of two and False otherwise. This is because, as explained above, the result of the bitwise AND operation will be 0 if n is a power of two, and the equality check == 0 will return True.

The comment # n & (n - 1) clears the least significant bit of n explains that the operation n & (n - 1) clears the least significant bit of n. This is another way of saying that it sets the least significant 1 in the binary representation of n to 0"""