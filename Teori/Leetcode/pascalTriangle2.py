# problem 119 : Pascal's Triangle 2
# Given a non-negative index k where k ≤ 33, return the kth index row of Pascal's triangle.

def getRow(rowIndex):
    row = [1]  # Initialize the current row with the first element
    
    for i in range(1, rowIndex + 1):
        prev_row = row.copy()  # Make a copy of the previous row
        row = [1]  # The first element of the current row is always 1
        
        # Calculate the remaining elements of the current row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)  # The last element of the current row is always 1
    
    return row
  
"""Here's how it works:

    We initialize the current row as [1], which is the first row of Pascal's triangle.
    For each subsequent row, we iterate from 1 to rowIndex: a. We make a copy of the current row, which will be used as the previous row for the next iteration. b. We reset the current row to [1], which is always the first element of each row in Pascal's triangle. c. We calculate the remaining elements of the current row by adding the corresponding elements from the previous row. d. We append 1 to the end of the current row, as the last element of each row in Pascal's triangle is always 1.
    After the loop finishes, we return the final row, which is the rowIndexth row of Pascal's triangle.

This algorithm uses O(rowIndex) extra space because we only store the current row and a copy of the previous row at any given time. The space complexity is optimal since we need to store the entire row to return it.

The time complexity of this algorithm is O(rowIndex^2) because we iterate over each row and each element within that row to calculate the values.
"""

# test the function
print(getRow(3))  # Output: [1, 3, 3, 1]
print(getRow(0))  # Output: [1]
print(getRow(5))  # Output: [1, 5, 10, 10, 5, 1]