# problem 290 : Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.
# Here, "follows" means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern(pattern, s):
    # Split the string s into words
    words = s.split()

    # Check if the lengths of pattern and words are different
    if len(pattern) != len(words):
        return False

    # Initialize dictionaries to store the mappings between pattern and words
    pattern_to_word = {}
    word_to_pattern = {}

    # Iterate over the pattern and words
    for char, word in zip(pattern, words):
        # Check if the current pattern character is already mapped to a different word
        if char in pattern_to_word and pattern_to_word[char] != word:
            return False

        # Check if the current word is already mapped to a different pattern character
        if word in word_to_pattern and word_to_pattern[word] != char:
            return False

        # Update the mappings
        pattern_to_word[char] = word
        word_to_pattern[word] = char

    return True
  
"""Here's how the algorithm works:

    We first split the string s into words using the split method.
    We check if the lengths of the pattern and words are different. If they are different, we return False, as s cannot follow the pattern.
    We then initialize two dictionaries pattern_to_word and word_to_pattern to store the mappings between pattern characters and words.
    We iterate over the pattern and words using the zip function to pair corresponding characters and words.
    For each pair, we check if the current pattern character is already mapped to a different word or if the current word is already mapped to a different pattern character. If either condition is met, we return False.
    If the mappings are consistent, we update the mappings in both dictionaries.
    If all mappings are consistent, we return True.
    
The time complexity of this algorithm is O(n), where n is the length of the input string s. This is because we iterate through the words once to create the mappings. The space complexity is also O(n), as we use two dictionaries to store the mappings between pattern characters and words.
"""

# Test cases
print(wordPattern("abba", "dog cat cat dog"))  # Output: True
print(wordPattern("abba", "dog cat cat fish"))  # Output: False
print(wordPattern("aaaa", "dog cat cat dog"))  # Output: False
print(wordPattern("abba", "dog dog dog dog"))  # Output: False
print(wordPattern("abc", "dog cat fish"))  # Output: True
print(wordPattern("ab", "dog dog"))  # Output: False
print(wordPattern("ab", "dog cat"))  # Output: True
print(wordPattern("ab", "dog fish"))  # Output: True
print(wordPattern("ab", "cat dog"))  # Output: True