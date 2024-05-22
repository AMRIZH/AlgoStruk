# problem 263 : Ugly Number
# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, and/or 5.

def isUgly(num):
    """
    Determines if a given number is an ugly number.
    """
    if num <= 0: # Check if the number is less than or equal to 0
        return False

    for prime in [2, 3, 5]:
        while num % prime == 0: # Check if the number is divisible by the prime factor
            num //= prime # Divide the number by the prime factor

    return num == 1 # Check if the number is equal to 1 after dividing by all prime factors
  
"""Here's how the algorithm works:

    We first check if the input number is less than or equal to 0. If it is, we return False, as ugly numbers are defined as positive numbers.
    We iterate through the prime factors 2, 3, and 5. For each prime factor, we divide the number by the prime factor as long as the number is divisible by the prime factor.
    After dividing by all prime factors, we check if the number is equal to 1. If it is, we return True, indicating that the number is an ugly number.
    
The time complexity of this algorithm is O(log n), where n is the input number. This is because the algorithm divides the number by the prime factors, which takes logarithmic time. The space complexity is O(1), as the algorithm uses a constant amount of extra space.
"""

# Test cases
print(isUgly(6))  # Output: True
print(isUgly(8))  # Output: True
print(isUgly(14))  # Output: False
print(isUgly(1))  # Output: True
print(isUgly(0))  # Output: False
print(isUgly(-6))  # Output: False
print(isUgly(30))  # Output: True
print(isUgly(45))  # Output: True
print(isUgly(49))  # Output: False
print(isUgly(50))  # Output: True
print(isUgly(100))  # Output: True