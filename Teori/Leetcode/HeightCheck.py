# problem 1051 Height Checker

def heightChecker(heights):
    sorted_heights = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != sorted_heights[i]:
            count += 1
    return count

heights = [1,1,4,2,1,3]

print(heightChecker(heights))

"""how the algorithm works:
    We first sort the heights list to get the expected order of the heights.
    We then iterate through the original heights list and compare each element with the corresponding element in the sorted list.
    If the two elements are not equal, we increment the count of students who need to move.
    Finally, we return the count of students who need to move.
    
    The time complexity of the algorithm is O(n log n) due to the sorting operation. The space complexity is O(n) as we create a sorted copy of the heights list."""
    
# Test cases
heights = [1,1,4,2,1,3]
assert heightChecker(heights) == 3
