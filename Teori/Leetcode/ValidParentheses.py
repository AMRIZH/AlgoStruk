def isValid(s): # s : string
    stack = [] # to store the opening brackets encountered.
    mapping = {")": "(", "}": "{", "]": "["} # maps closing brackets to their corresponding opening brackets.

    for char in s: # iterate through each character in the input string.
        if char in mapping: # if the character is a closing bracket.
            top_element = stack.pop() if stack else '#' # pop the top element from the stack if it is not empty, otherwise assign '#' to top_element.
            if mapping[char] != top_element: # if the mapping of the current closing bracket does not match the top element of the stack.
                return False # return False, as the brackets are not valid.
        else:
            stack.append(char) # if the character is an opening bracket, push it onto the stack.

    return len(stack) == 0 # return True if the stack is empty after processing all characters, otherwise return False.
  
  
"""Here's how the code works:

    We create an empty list stack to store the opening brackets encountered.
    We create a dictionary mapping that maps closing brackets to their corresponding opening brackets.
    We iterate through each character char in the input string s.
    If char is a closing bracket (i.e., char is a key in the mapping dictionary):
        We pop the top element from the stack (or assign a special value '#' if the stack is empty).
        If the popped element is not the corresponding opening bracket for char (as specified in the mapping dictionary), we return False because the brackets are not balanced.
    If char is an opening bracket, we push it onto the stack.
    After iterating through the entire string, we check if the stack is empty. If it's empty, it means all opening brackets have been properly closed, so we return True. Otherwise, we return False.
    
This algorithm has a time complexity of O(n), where n is the length of the input string s, because we iterate through each character in the string once. The space complexity is also O(n) because the stack can store at most n elements."""

# test case
print(isValid("()"))        # Output: True
print(isValid("()[]{}"))    # Output: True
print(isValid("(]"))        # Output: False
print(isValid("([)]"))      # Output: False
print(isValid("{[]}"))      # Output: True