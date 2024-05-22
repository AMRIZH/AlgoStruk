class Stack:
  def __init__(self):
    self.items = []  # Initialize an empty list to store the stack items
    
  def isEmpty(self):
    return len(self.items) == 0  # Check if the stack is empty
  
  def __len__(self):
    return len(self.items)  # Get the length of the stack
  
  def peek(self):
    assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"  # Check if the stack is empty
    return self.items[-1]  # Return the top item of the stack
  
  def pop(self):
    assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"  # Check if the stack is empty
    return self.items.pop()  # Remove and return the top item of the stack
  
  def push(self, item):
    self.items.append(item)  # Add an item to the top of the stack
    
def isPalindrome(word):
  if len(word) < 2:
    return True  # Base case: if the word has less than 2 characters, it is a palindrome
  if word[0] != word[-1]:
    return False  # If the first and last characters of the word are different, it is not a palindrome
  return isPalindrome(word[1:-1])  # Recursively check if the word without the first and last characters is a palindrome

def isPalindromeStack(word): 
  f = Stack()  # Create a new stack object
  for i in range(len(word)):
    f.push(word[i])  # Push each character of the word onto the stack
  for i in range(len(word)): 
    if f.pop() != word[i]:  # Pop each character from the stack and compare it with the corresponding character in the word
      return False  # If any characters don't match, it is not a palindrome
  return True  # If all characters match, it is a palindrome
  
if isPalindromeStack("katak"):
  print("Palindrome")
else:
  print("Bukan Palindrome")