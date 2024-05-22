# problem 205 : Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s: str, t: str) -> bool:
    """
    Returns True if the given strings s and t are isomorphic, False otherwise.
    """
    # Initialize dictionaries to store mappings from s to t and t to s
    s_to_t = {}
    t_to_s = {}
    
    # Iterate through the characters of s and t
    for char_s, char_t in zip(s, t):
        # Check if the mapping from s to t is consistent
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check if the mapping from t to s is consistent
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

"""Here's how the algorithm works:

    We initialize two dictionaries s_to_t and t_to_s to store mappings from s to t and t to s, respectively.
    We iterate through the characters of s and t using the zip function to pair corresponding characters.
    For each pair of characters, we check if the mapping from s to t is consistent. If the character char_s is already mapped to a different character than char_t, we return False.
    We do the same for the mapping from t to s, ensuring that the mappings are consistent in both directions.
    If all mappings are consistent, we return True.
    
    The time complexity of this algorithm is O(n), where n is the length of the input strings s and t. This is because we iterate through the characters of both strings once. The space complexity is also O(n), as we use two dictionaries to store the mappings between characters.
    """

# Test cases
print(isIsomorphic("egg", "add"))  # Output: True
print(isIsomorphic("foo", "bar"))  # Output: False
print(isIsomorphic("paper", "title"))  # Output: True
print(isIsomorphic("ab", "aa"))  # Output: False
print(isIsomorphic("badc", "baba"))  # Output: False
print(isIsomorphic("ab", "ca"))  # Output: True
print(isIsomorphic("ab", "cd"))  # Output: True
print(isIsomorphic("ab", "ef"))  # Output: True
print(isIsomorphic("ab", "cd"))  # Output: True