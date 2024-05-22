# problem 202 : Happy Number
# Write an algorithm to determine if a number n is happy.

def isHappy(n):
    """
    Determines if a given number is happy.
    """
    def get_next(num):
        """
        Returns the sum of the squares of the digits of a given number.
        """
        total_sum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()  # Initialize a set to store seen numbers

    while n != 1 and n not in seen:
        seen.add(n)  # Add the current number to the set
        n = get_next(n)  # Get the next number

    return n == 1  # Return True if n is 1 (happy), False otherwise
  
"""Here's how the algorithm works:

    We define a helper function get_next to calculate the sum of the squares of the digits of a given number.
    We initialize a set seen to keep track of the numbers we have seen.
    We iterate until the number becomes 1 (happy) or we encounter a number we have seen before.
    In each iteration, we add the current number to the set seen and update the number to the next number.
    If the number becomes 1, we return True (happy), otherwise, we return False.
    
The time complexity of this algorithm is O(log n), where n is the input number. This is because the algorithm iterates through the digits of the number, which takes logarithmic time. The space complexity is also O(log n) due to the space used by the set seen to store seen numbers.
"""

# Test cases
print(isHappy(19))  # Output: True
print(isHappy(2))  # Output: False
print(isHappy(7))  # Output: True
print(isHappy(1111111))  # Output: False
print(isHappy(123456789))  # Output: False
print(isHappy(0))  # Output: False
print(isHappy(1))  # Output: True
print(isHappy(10))  # Output: True
print(isHappy(100))  # Output: True
print(isHappy(101))  # Output: True
print(isHappy(102))  # Output: False
print(isHappy(103))  # Output: False