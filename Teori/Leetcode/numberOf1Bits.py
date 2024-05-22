# problem 191 : Number of 1 Bits
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

def hammingWeight(n):
    """
    Counts the number of '1' bits in the binary representation of a given integer.
    """
    count = 0  # Initialize the count of '1' bits

    # Iterate through the bits of the input integer
    while n:
        count += n & 1  # Increment count if the last bit is 1
        n >>= 1  # Right shift the input integer by 1 bit

    return count  # Return the total count of '1' bits
  
"""Here's how the algorithm works:

    We initialize the count of '1' bits to 0.
    We iterate through the bits of the input integer n.
    For each iteration, we increment the count if the last bit of n is 1.
    We then right-shift the input integer n by 1 bit to process the next bit.
    After processing all bits, we return the total count of '1' bits.
    
The time complexity of this algorithm is O(log n), where n is the input integer. This is because we iterate through the bits of the input integer, which takes logarithmic time. The space complexity is O(1), as we are using a constant amount of extra space.
"""

# Test cases
print(hammingWeight(11))  # Output: 3
print(hammingWeight(128))  # Output: 1
print(hammingWeight(4294967293))  # Output: 31
print(hammingWeight(0))  # Output: 0
print(hammingWeight(1))  # Output: 1
print(hammingWeight(2147483648))  # Output: 1
print(hammingWeight(1431655765))  # Output: 16
print(hammingWeight(858993459))  # Output: 14
print(hammingWeight(4294967295))  # Output: 32
print(hammingWeight(255))  # Output: 8
print(hammingWeight(65535))  # Output: 16
print(hammingWeight(131071))  # Output: 17
print(hammingWeight(262143))  # Output: 18