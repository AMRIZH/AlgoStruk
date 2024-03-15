def longest_common_prefix(strs):
    if not strs:
        return ""

    # Find the shortest string in the array
    shortest = min(strs, key=len)

    # Iterate over the characters of the shortest string
    for i, char in enumerate(shortest):
        # Check if all other strings have the same character at this position
        for other in strs:
            if other[i] != char:
                return shortest[:i]

    # If all strings have the same prefix, return the shortest string
    return shortest