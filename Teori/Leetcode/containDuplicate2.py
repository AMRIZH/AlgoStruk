# problem 219 : Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate(nums, k):
    """
    Returns True if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, False otherwise.
    """
    # Create a dictionary to store the indices of elements
    indices = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Check if the element is already in the dictionary
        if num in indices:
            # Check the difference between the current index and the previous index
            if i - indices[num] <= k:
                return True
        
        # Update the index of the element
        indices[num] = i
    
    # No duplicates found
    return False
  
"""Here's how the algorithm works:

    We create a dictionary indices to store the indices of elements encountered in the array.
    We iterate through the input array nums using the enumerate function to get both the index i and the element num.
    For each element, we check if it is already in the dictionary indices.
    If the element is already in the dictionary, we check the difference between the current index i and the previous index indices[num].
    If the difference is less than or equal to k, we return True.
    If no duplicates are found within the specified range, we update the index of the element in the dictionary.
    If no duplicates are found, we return False.
    
    The time complexity of this algorithm is O(n), where n is the length of the input array nums. This is because we iterate through the array once and perform constant-time operations on the dictionary. The space complexity is also O(n), as the dictionary can store up to n unique elements."""
    
# Test cases
print(containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
print(containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: True
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 3))  # Output: True
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 4))  # Output: True
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 5))  # Output: True
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 6))  # Output: True
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 7))  # Output: True