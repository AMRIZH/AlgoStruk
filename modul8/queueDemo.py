from queue import Queue, PriorityQueue

# initialize the queue
que = Queue()
# enqueue some data
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
# check if the queue is empty
print("Is the queue empty?", que.isEmpty())
# check the length of the queue
print("Length of the queue:", len(que))
# get the front most element
print("Front most element:", que.getFrontMost())
# get the rear most element
print("Rear most element:", que.getRearMost())
# dequeue elements and print them
print("Dequeued element:", que.dequeue())
print("Dequeued element:", que.dequeue())
print("Dequeued element:", que.dequeue())
print("Dequeued element:", que.dequeue())
print("Dequeued element:", que.dequeue())
# check if the queue is empty after dequeuing all elements
print("Is the queue empty?", que.isEmpty())
# try to get front most element from an empty queue
print("Front most element from empty queue:", que.getFrontMost())

# Initialize the priority queue
pq = PriorityQueue()

# Enqueue some dummy data
pq.enqueue('task1', 5)
pq.enqueue('task2', 3)
pq.enqueue('task3', 4)
pq.enqueue('task4', 1)
pq.enqueue('task5', 2)
pq.enqueue('task6', -1)  # Same priority as 'task4'

# Check if the queue is empty
print("Is the queue empty?", pq.isEmpty())  # Expected: False

# Check the length of the queue
print("Length of the queue:", len(pq))  # Expected: 6

# Dequeue elements and print them
print("Dequeued element:", pq.dequeue())  # Expected: 'task4' (priority 1)
print("Dequeued element:", pq.dequeue())  # Expected: 'task6' (priority 1)
print("Dequeued element:", pq.dequeue())  # Expected: 'task5' (priority 2)
print("Dequeued element:", pq.dequeue())  # Expected: 'task2' (priority 3)
print("Dequeued element:", pq.dequeue())  # Expected: 'task3' (priority 4)
print("Dequeued element:", pq.dequeue())  # Expected: 'task1' (priority 5)

# Check if the queue is empty after dequeuing all elements
print("Is the queue empty?", pq.isEmpty())  # Expected: True

