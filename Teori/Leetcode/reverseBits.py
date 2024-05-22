# problem 190 : Reverse Bits
# Given an integer n, return the number obtained by reversing its bits.
def reverseBits(n):
    """
    Reverses the bits of a given 32-bit unsigned integer.
    """
    # Initialize the result
    result = 0

    # Iterate through the 32 bits
    for i in range(32):
        # Extract the current bit from the input
        bit = (n >> i) & 1

        # Shift the result left by 1 and add the current bit
        result = (result << 1) | bit

    return result
  
"""Here's how the algorithm works:

    We initialize the result to 0.
    We iterate through the 32 bits of the input integer n.
    For each bit position i, we extract the ith bit from n by right-shifting n by i and taking the bitwise AND with 1.
    We shift the result left by 1 and add the extracted bit to the rightmost position.
    After processing all 32 bits, we return the final result.
    
The time complexity of this algorithm is O(1), as we are iterating through a fixed number of bits (32 bits for a 32-bit integer). The space complexity is also O(1), as we are using a constant amount of extra space.
"""

# Test cases
print(reverseBits(43261596))  # Output: 964176192
print(reverseBits(4294967293))  # Output: 3221225471
print(reverseBits(0))  # Output: 0
print(reverseBits(1))  # Output: 2147483648
print(reverseBits(2147483648))  # Output: 1
print(reverseBits(1431655765))  # Output: 2863311530
print(reverseBits(858993459))  # Output: 286331153