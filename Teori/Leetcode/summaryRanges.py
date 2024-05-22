# problem 228 : Summary Ranges
# Given a sorted integer array nums, where the range of elements are in the inclusive range [0, 99], return the summary of its ranges.

def summaryRanges(nums):
    """
    Returns the summary of ranges in the given sorted integer array.
    """
    # Initialize the result list
    result = []
    
    # Initialize the start and end of the current range
    start = end = nums[0]
    
    # Iterate through the array
    for i in range(1, len(nums)):
        # Check if the current element is part of the current range
        if nums[i] == end + 1:
            end = nums[i]
        else:
            # Add the current range to the result list
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            
            # Update the start and end of the new range
            start = end = nums[i]
    
    # Add the last range to the result list
    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}->{end}")
    
    return result
  
"""Here's how the algorithm works:

    We initialize the result list to store the summary of ranges.
    We initialize the start and end variables to keep track of the current range.
    We iterate through the input array nums starting from the second element.
    For each element, we check if it is part of the current range by comparing it with the previous element.
    If the current element is part of the current range, we update the end of the range.
    If the current element is not part of the current range, we add the current range to the result list and update the start and end of the new range.
    After processing all elements, we add the last range to the result list.
    We return the result list containing the summary of ranges.
    
The time complexity of this algorithm is O(n), where n is the length of the input array nums. This is because we iterate through the array once and perform constant-time operations. The space complexity is also O(n), as the result list can store up to n ranges."""

# Test cases
print(summaryRanges([0, 1, 2, 4, 5, 7]))  # Output: ["0->2", "4->5", "7"]
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # Output: ["0", "2->4", "6", "8->9"]
print(summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: ["0->9"]
print(summaryRanges([0]))  # Output: ["0"]
print(summaryRanges([0, 1, 2, 3, 5, 6, 7, 9]))  # Output: ["0->3", "5->7", "9"]
print(summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 9]))  # Output: ["0->7", "9"]
print(summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8]))  # Output: ["0->8"]
print(summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: ["0->10"]
print(summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))  # Output: ["0->9", "11"]
print(summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]))  # Output: ["0->9", "11->12"]
print(summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]))  # Output: ["0->9", "11", "13"]