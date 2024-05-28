class Stack:
  def __init__(self):
    self.items = []  # Initialize an empty list to store the stack items
    
  def isEmpty(self):
    return len(self.items) == 0  # Check if the stack is empty
  
  def __len__(self):
    return len(self.items)  # Get the length of the stack
  
  def pop(self):
    assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"  # Check if the stack is empty
    return self.items.pop()  # Remove and return the top item of the stack
  
  def push(self, data):
    self.items.append(data)  # Add an item to the top of the stack

def isPalindromeStack(word): 
  f = Stack()  # Create a new stack object
  for i in range(len(word)):
    f.push(word[i])  # Push each character of the word onto the stack
  for i in range(len(word)): 
    if f.pop() != word[i]:  # Pop each character from the stack and compare it with the corresponding character in the word
      return False  # If any characters don't match, it is not a palindrome
  return True  # If all characters match, it is a palindrome

while True :
  A = input("Masukkan kata : ")
  if A == "k" :
    break
  if isPalindromeStack(A):
    print("Palindrome")
  else:
    print("Bukan Palindrome")