# problem 88 : merge sorted array
def merge(nums1, m: int, nums2, n: int) -> None: # nums1 ,nums2 are lists of integers, m, n are integers
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Merge the two arrays from the end
    p1 = m - 1  # Pointer for the last valid element in nums1
    p2 = n - 1  # Pointer for the last valid element in nums2
    p = m + n - 1  # Pointer for the last index of the merged array

    # If nums1 is empty, copy nums2 into nums1
    if m == 0: 
        nums1[:] = nums2
        return

    while p1 >= 0 and p2 >= 0: # While there are elements in both arrays
        if nums1[p1] >= nums2[p2]: # Compare the elements from the end
            nums1[p] = nums1[p1] # Copy the larger element to nums1
            p1 -= 1 # Move the pointer to the left
        else:
            nums1[p] = nums2[p2] # Copy the larger element to nums1
            p2 -= 1 # Move the pointer to the left
        p -= 1 # Move the pointer to the left

    # If there are remaining elements in nums2, copy them to nums1
    if p2 >= 0: 
        nums1[:p2 + 1] = nums2[:p2 + 1] # Copy the remaining elements to nums1
        
"""
Here's how the updated code works:

    We initialize three pointers: p1 pointing to the last valid element in nums1 (index m-1), p2 pointing to the last valid element in nums2 (index n-1), and p pointing to the last index of the merged array (m+n-1).
    We check if nums1 is empty (i.e., m=0). If it is, we simply copy nums2 into nums1 using slice assignment: nums1[:] = nums2, and then return.
    If nums1 is not empty, we proceed with the merge as before:
        We merge the two arrays from the end by comparing the elements at p1 and p2. The larger element is placed at the pth position in nums1, and the corresponding pointer (p1 or p2) is decremented.
    After the while loop, if there are remaining elements in nums2 (i.e., p2 >= 0), we copy them to the beginning of nums1 using slice assignment: nums1[:p2 + 1] = nums2[:p2 + 1].

With this update, the code now correctly handles the case where nums1 is empty (m=0) and nums2 has elements (n>0) by copying nums2 into nums1. The time complexity of the updated code remains O(m+n), where m and n are the lengths of nums1 and nums2, respectively.
"""
# test case
nums1 = [0]
nums2 = [1]
merge(nums1, 0, nums2, 1)
print(nums1)  # Output: [1]

# improved code
def merge(nums1, m: int, nums2, n: int) -> None: # nums1 ,nums2 are lists of integers, m, n are integers
    if m == 0: # if nums1 is empty, copy nums2 into nums1
        nums1[:] = nums2 # copy nums2 into nums1
        return # exit the function
    cur = len(nums1) - 1 # set the current index to the last index of nums1
    while m and n: # while there are elements in both arrays
        if nums2[n-1] >= nums1[m-1]: # compare the elements from the end
            nums1[cur] = nums2[n-1] # copy the larger element to nums1
            n -= 1 # move the pointer to the left
        else: # copy the larger element to nums1
            nums1[cur] = nums1[m-1] # copy the larger element to nums1
            m -= 1 # move the pointer to the left
        cur -= 1 # move the pointer to the left
    # exit, then paste all others, if m, then no need to copy
    if n: # if there are remaining elements in nums2
        nums1[:n] = nums2[:n] # copy the remaining elements to nums1
        
"""
Explanation:

    We start by checking if nums1 is empty (i.e., m=0). If it is, we copy nums2 into nums1 using slice assignment: nums1[:] = nums2, and then return.
    If nums1 is not empty, we proceed with the merge as before:
        We set the current index cur to the last index of nums1.
        We iterate while there are elements in both arrays (m and n).
        We compare the elements from the end of both arrays and copy the larger element to nums1 at index cur. We then decrement the corresponding pointer (m or n) and the current index cur.
    After the while loop, if there are remaining elements in nums2 (i.e., n>0), we copy them to the beginning of nums1 using slice assignment: nums1[:n] = nums2[:n]. This step ensures that any remaining elements in nums2 are copied to the beginning of nums1. The time complexity of the updated code remains O(m+n), where m and n are the lengths of nums1 and nums2, respectively. The space complexity is O(1) since we are modifying the input array nums1 in-place. """