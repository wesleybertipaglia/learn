# Ordered: Yes
# Mutable: Yes
# Duplicates: Yes
# Indexing: No (but can be achieved through traversal)
# Different Data Types: Yes

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Add new node at the end
    def append(self, value):
        new_node = Node(value)

        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Otherwise, traverse to the end of the list and append the new node
        current = self.head # head
        while current.next:
            current = current.next # head -> ...            
        current.next = new_node # head -> ... -> new_node

    # Add new node at the beginning
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Remove a node
    def remove(self, value):
        # Check if the list is empty
        if not self.head:
            return
        
        # Check if the head is the node to be removed
        if self.head.value == value:
            self.head = self.head.next
            return
        
        # Otherwise, traverse the list to find the node to be removed
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    # Print the linked list
    def print(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')
