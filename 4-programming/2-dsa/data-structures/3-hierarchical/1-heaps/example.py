# Ordered: Partially (a heap maintains a specific ordering property, not a complete order)
# Mutable: Yes
# Duplicates: Yes
# Indexing: Indirectly (by position, but typically accessed via heap operations)
# Different Data Types: Yes (but typically elements are comparable)

import heapq

# Create a list to use as a heap
heap = []

# Add elements to the heap (push)
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 7)

# Print the heap
print(heap)  # Output: [1, 7, 5, 10]

# Peek at the smallest element
print(heap[0])  # Output: 1

# Remove the smallest element (pop)
smallest = heapq.heappop(heap)
print(smallest)  # Output: 1
print(heap)      # Output: [5, 7, 10]

# Add and remove elements simultaneously (pushpop)
second_smallest = heapq.heappushpop(heap, 2)
print(second_smallest)  # Output: 2
print(heap)             # Output: [5, 7, 10]

# Convert an existing list into a heap
numbers = [20, 1, 15, 5, 10]
heapq.heapify(numbers)
print(numbers)  # Output: [1, 5, 15, 20, 10]

# Find the n largest elements
largest_elements = heapq.nlargest(3, numbers)
print(largest_elements)  # Output: [20, 15, 10]

# Find the n smallest elements
smallest_elements = heapq.nsmallest(3, numbers)
print(smallest_elements)  # Output: [1, 5, 10]
