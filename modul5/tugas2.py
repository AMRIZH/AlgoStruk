def merge_sorted_arrays(A, B):
    """Merge two sorted arrays A and B into a single sorted array C."""
    C = []
    i, j = 0, 0
    # Traverse both arrays and append the smaller element to C
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    # Append remaining elements from A or B
    C.extend(A[i:])
    C.extend(B[j:])
    return C

# Example usage
A = [1, 3, 5, 7]
B = [2, 4, 6, 8, 10]

C = merge_sorted_arrays(A, B)
print("Array C:", C)