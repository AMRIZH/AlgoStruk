# problem 268 : Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(nums):
    """
    Returns the missing number in the given array.
    """
    n = len(nums) # Get the length of the input array
    expected_sum = n * (n + 1) // 2 # Calculate the expected sum of numbers from 0 to n ~ gunakan prinsip segitiga
    actual_sum = sum(nums) # Calculate the actual sum of numbers in the input array
    return expected_sum - actual_sum # Return the missing number
  
"""Here's how the algorithm works:

    We calculate the expected sum of numbers from 0 to n using the formula n * (n + 1) // 2.
    We calculate the actual sum of the numbers in the input array nums using the sum function.
    The missing number is the difference between the expected sum and the actual sum.
    We return the missing number as the output.
    
The time complexity of this algorithm is O(n), where n is the length of the input array nums. This is because we iterate through the array once to calculate the actual sum. The space complexity is O(1), as the algorithm uses a constant amount of extra space.
"""

# Test cases
print(missingNumber([3, 0, 1]))  # Output: 2
print(missingNumber([0, 1]))  # Output: 2
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Output: 8
print(missingNumber([0]))  # Output: 1
print(missingNumber([1]))  # Output: 0
print(missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 9]))  # Output: 8
print(missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8]))  # Output: 9
print(missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 10
print(missingNumber([0, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 1