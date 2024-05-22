import collections
# problem 225 : Implement Stack using Queues
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:
#     void push(int x) Pushes element x to the top of the stack.
#     int pop() Removes the element on the top of the stack and returns it.
#     int top() Returns the element on the top of the stack.
#     boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
#     You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
class MyStack:
    def __init__(self):
      """
      Initialize your data structure here.
      """
      self.queue = collections.deque()

    def push(self, x: int) -> None:
      """
      Push element x onto stack.
      """
      self.queue.append(x)
      # Rotate the queue to make the newly added element the front
      for _ in range(len(self.queue) - 1):
        self.queue.append(self.queue.popleft())

    def pop(self) -> int:
      """
      Removes the element on top of the stack and returns that element.
      """
      return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue

"""Here's how the algorithm works:

    We use a deque (double-ended queue) to implement the stack.
    The push operation is straightforward: we append the new element to the deque and then rotate the deque to make the newly added element the front.
    The pop operation removes and returns the element at the front of the deque.
    The top operation returns the element at the front of the deque without removing it.
    The empty operation checks if the deque is empty and returns True if it is, False otherwise.
    
    The time complexity of the push operation is O(n), where n is the number of elements in the stack. This is because we rotate the deque to make the newly added element the front. The time complexity of the pop, top, and empty operations is O(1), as they involve constant-time operations on the deque. The space complexity is O(n), as the deque can store up to n elements."""
    
# Test cases
stack = MyStack()
stack.push(1)
stack.push(2)
assert stack.top() == 2
assert stack.pop() == 2
assert not stack.empty()
assert stack.pop() == 1
assert stack.empty()

stack.push(3)
stack.push(4)
assert stack.top() == 4
assert stack.pop() == 4
assert not stack.empty()
assert stack.pop() == 3
assert stack.empty()
print("All test cases pass")

# Output: All test cases pass