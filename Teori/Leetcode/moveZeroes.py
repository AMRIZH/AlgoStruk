# problem 283 : Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    """
    Moves all zeroes to the end of the given integer array in-place.
    """
    # Initialize a pointer to keep track of the position to place the next non-zero element
    insert_pos = 0
    
    # Iterate through the array
    for num in nums:
        # If the current element is non-zero, move it to the insert position
        if num != 0: 
            nums[insert_pos] = num 
            insert_pos += 1 
    
    # Fill the remaining positions with zeroes
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
    return nums

"""Here's how the algorithm works:
  
    We initialize a pointer insert_pos to keep track of the position to place the next non-zero element.
    We iterate through the input array nums.
    For each non-zero element, we move it to the insert position and increment the insert position.
    After processing all elements, we fill the remaining positions with zeroes.
    We return the modified array nums.
    
The time complexity of this algorithm is O(n), where n is the length of the input array nums. This is because we iterate through the array once and perform constant-time operations. The space complexity is O(1), as we are using a constant amount of extra space."""

# Test cases
print(moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(moveZeroes([0]))  # Output: [0]
print(moveZeroes([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(moveZeroes([0, 0, 0, 0, 0]))  # Output: [0, 0, 0, 0, 0]
print(moveZeroes([1, 0, 0, 0, 0]))  # Output: [1, 0, 0, 0, 0]