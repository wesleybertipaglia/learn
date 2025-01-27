# Ordered: Yes
# Mutable: Yes
# Duplicates: Yes
# Indexing: Yes (though typically not used)
# Different Data Types: Yes

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Enqueue an element to the back of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Dequeue an element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.popleft()

    # Peek at the front element of the queue
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.items[0]

    # Get the size of the queue
    def size(self):
        return len(self.items)

    # Print the queue
    def print_queue(self):
        print(list(self.items))

# Create a queue and perform operations
queue = Queue()
queue.enqueue(1)
queue.enqueue('hello')
queue.enqueue(3.14)
queue.enqueue(True)
queue.print_queue()  # Output: [1, 'hello', 3.14, True]

print(queue.peek())  # Output: 1
queue.dequeue()
queue.print_queue()  # Output: ['hello', 3.14, True]

print(queue.size())  # Output: 3
