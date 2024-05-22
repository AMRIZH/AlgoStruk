# problem 118 : Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
def generate_pascal_triangle(numRows):
    triangle = []
    
    for row in range(numRows):
        row_values = [1] * (row + 1)  # Initialize the row with 1s
        
        for i in range(1, row):
            prev_row = triangle[row - 1]
            row_values[i] = prev_row[i - 1] + prev_row[i]
        
        triangle.append(row_values)
    
    return triangle
  
"""Here's how the code works:

    We initialize an empty list triangle to store the rows of Pascal's triangle.
    We use a for loop to iterate numRows times, where each iteration represents a new row in the triangle.
    For each row, we first initialize a list row_values with row + 1 ones. This is because each row starts and ends with 1.
    We then use another for loop to fill in the middle values of the row. For each index i from 1 to row - 1:
        We retrieve the previous row from the triangle list (prev_row = triangle[row - 1]).
        We calculate the value of row_values[i] by summing the values at indices i - 1 and i from the previous row (row_values[i] = prev_row[i - 1] + prev_row[i]).
    After filling in the values for the current row, we append the row_values list to the triangle list.
    Finally, we return the triangle list, which contains all the rows of Pascal's triangle up to numRows.

The time complexity of this solution is O(numRows^2), as we need to iterate over each row and each element within that row to calculate the values.

The space complexity is O(numRows^2), as we are storing all the rows of Pascal's triangle in the triangle list.
"""

# test the function
print(generate_pascal_triangle(5))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

print(generate_pascal_triangle(1))
# Output: [[1]]

print(generate_pascal_triangle(10))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]