# problem 28
def strStr(haystack: str, needle: str) -> int:
    if not needle: # if needle is an empty string
        return 0 # return 0 as per the problem statement

    needle_len = len(needle) # length of the needle
    haystack_len = len(haystack) # length of the haystack

    lps = [0] * needle_len # initialize the lps list with zeros

    # Precompute the longest proper prefix that is also a suffix
    prev_lps, i = 0, 1 # initialize variables
    while i < needle_len: # iterate through the needle
        if needle[i] == needle[prev_lps]: # if the characters match
            lps[i] = prev_lps + 1 # update the lps value
            prev_lps += 1 # increment prev_lps
            i += 1 # increment i
        elif prev_lps == 0: # if no proper prefix is found
            lps[i] = 0 # set lps value to 0
            i += 1  # increment i
        else: # if characters don't match
            prev_lps = lps[prev_lps - 1] # update prev_lps

    # Search for the needle in the haystack
    i, j = 0, 0 # initialize variables
    while i < haystack_len: # iterate through the haystack
        if haystack[i] == needle[j]: # if characters match
            i += 1 # increment i
            j += 1 # increment j
            if j == needle_len: # if the needle is found
                return i - j # return the index of the first occurrence
        else: # if characters don't match
            if j == 0: # if no proper prefix is found
                i += 1 # increment i
            else: # if proper prefix is found
                j = lps[j - 1] # update j using lps information

    return -1 # return -1 if needle is not found
  
"""Here's how the code works:

    First, we handle the edge case where the needle is an empty string. In this case, we return 0 as per the problem statement.
    We initialize variables to store the lengths of the needle and haystack strings.
    We create a list lps (Longest Proper Prefix that is also a Suffix) of the same length as needle. This list will store the lengths of the longest proper prefixes that are also suffixes for each prefix of the needle string. This information is used to avoid redundant comparisons during the search phase.
    We precompute the lps list using a helper function. This step has a time complexity of O(m), where m is the length of the needle.
    We then search for the needle in the haystack using the precomputed lps information. This step has a time complexity of O(n), where n is the length of the haystack.
    If the needle is found, we return the index of its first occurrence in the haystack. Otherwise, we return -1.

The overall time complexity of this algorithm is O(m + n), where m is the length of the needle and n is the length of the haystack. The space complexity is O(m) to store the lps list.
"""

# test cases
print(strStr("sadbutsad", "sad"))  # Output: 0
print(strStr("leetcode", "leeto"))  # Output: -1
print(strStr("hello", "ll"))  # Output: 2
print(strStr("aaaaa", "bba"))  # Output: -1