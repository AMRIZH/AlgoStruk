# problem 292 : Nim Game
# You are playing the following Nim Game with your friend:

# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# The one who removes the last stone is the winner.
# Given the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

def canWinNim(n: int) -> bool:
    """
    Determines if you can win the Nim Game with n stones.
    """
    return n % 4 != 0 # Check if the number of stones is not a multiple of 4
  
"""Here's how the algorithm works:

    If the number of stones n is a multiple of 4, you will lose the game, as your friend can always remove the appropriate number of stones to leave you with a multiple of 4 stones.
    If the number of stones n is not a multiple of 4, you can win the game by removing the appropriate number of stones to leave your friend with a multiple of 4 stones.
    
    The time complexity of this algorithm is O(1), as it involves a single arithmetic operation. The space complexity is also O(1), as the algorithm uses a constant amount of extra space."""
    
# Test cases
print(canWinNim(4))  # Output: False
print(canWinNim(1))  # Output: True
print(canWinNim(2))  # Output: True
print(canWinNim(3))  # Output: True
print(canWinNim(5))  # Output: True