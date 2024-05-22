# problem 169 : Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(nums):
    """
    Returns the majority element in the given array.
    """
    # Initialize the candidate and count
    candidate = None
    count = 0

    # Find the candidate majority element
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Verify if the candidate is the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    # If count is greater than n/2, return the candidate
    if count > len(nums) // 2:
        return candidate

    # No majority element found
    return -1
  
"""Here's how the algorithm works:

    We initialize the candidate and count variables to keep track of the majority element and its count.
    We iterate through the input array nums and update the candidate and count based on the current element.
    We then verify if the candidate is the majority element by counting its occurrences in the array.
    If the count of the candidate is greater than n/2, where n is the length of the array, we return the candidate as the majority element.
    If no majority element is found, we return -1.
    
    The time complexity of this algorithm is O(n), where n is the length of the input array nums. This is because we iterate through the array twice, once to find the candidate majority element and once to verify its count. The space complexity is O(1), as we are using a constant amount of extra space."""
    
# test case
print(majorityElement([3, 2, 3]))  # Output: 3
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(majorityElement([1]))  # Output: 1
print(majorityElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))  # Output: 1
print(majorityElement([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))  # Output: 3
print(majorityElement([-1, -1, -1, 1, 1, 1, 1]))  # Output: 1