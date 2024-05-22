# problem 217 : Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    """
    Returns True if any value appears at least twice in the array, False otherwise.
    """
    # Create a set to store unique elements
    unique_elements = set()
    
    # Iterate through the array
    for num in nums:
        # If the element is already in the set, return True
        if num in unique_elements:
            return True
        
        # Add the element to the set
        unique_elements.add(num)
    
    # No duplicates found
    return False

"""Here's how the algorithm works:

    We create a set unique_elements to store unique elements encountered in the array.
    We iterate through the input array nums and check if each element is already in the set.
    If we find a duplicate element, we return True.
    If no duplicates are found, we return False.
    
    The time complexity of this algorithm is O(n), where n is the length of the input array nums. This is because we iterate through the array once and perform constant-time operations on the set. The space complexity is also O(n), as the set can store up to n unique elements."""
    
# Test cases
print(containsDuplicate([1, 2, 3, 1]))  # Output: True
print(containsDuplicate([1, 2, 3, 4]))  # Output: False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: False
print(containsDuplicate([1, 1, 1, 1, 1, 1, 1, 1, 1]))  # Output: True
print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))  # Output: True
print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # Output: False
print(containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]))  # Output: True