# problem 242 : Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s: str, t: str) -> bool:
    """
    Returns True if t is an anagram of s, False otherwise.
    """
    # Check if the lengths of the strings are equal
    if len(s) != len(t):
        return False
    
    # Initialize dictionaries to store character frequencies
    s_freq = {}
    t_freq = {}
    
    # Count the frequencies of characters in s
    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1 # Increment the frequency by 1 or set it to 1 if not present
    
    # Count the frequencies of characters in t
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1 # Increment the frequency by 1 or set it to 1 if not present
    
    # Check if the frequencies of characters are the same
    return s_freq == t_freq
  
"""Here's how the algorithm works:

    We first check if the lengths of the input strings s and t are equal. If they are not equal, we return False, as t cannot be an anagram of s.
    We then initialize two dictionaries s_freq and t_freq to store the frequencies of characters in s and t, respectively.
    We count the frequencies of characters in s and t using the get method to handle cases where the character is not yet in the dictionary.
    Finally, we compare the dictionaries s_freq and t_freq to check if the frequencies of characters are the same. If they are the same, we return True; otherwise, we return False.
    
    The time complexity of this algorithm is O(n), where n is the length of the input strings s and t. This is because we iterate through the characters of both strings once to count the frequencies. The space complexity is also O(n), as we use two dictionaries to store the frequencies of characters in the strings."""
    
# Test cases
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))  # Output: False
print(isAnagram("listen", "silent"))  # Output: True
print(isAnagram("hello", "world"))  # Output: False
print(isAnagram("abc", "cba"))  # Output: True
print(isAnagram("abc", "def"))  # Output: False
