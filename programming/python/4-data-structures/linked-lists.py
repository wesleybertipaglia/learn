# linked lists
# ordered, mutable, allow duplicates
# data types: different types of data
# stored: in nodes
# size: dynamic

# linked lists are a collection of nodes that are connected to each other
# each node contains data and a reference to the next node in the sequence
# the first node is called the head and the last node is called the tail
# the tail node points to None
# the head node points to the next node in the sequence

# linked lists are useful when you need to add or remove items frequently
# they are slower than arrays when searching for items
# they are faster than arrays when adding or removing items

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Linked List"""
    def __init__(self):
        self.head = None
    
    def add(self, data):
        """Add a node to the beginning of the linked list (O(1))"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node # list is empty -> [new_node]
            return
        else:
            new_node.next = self.head # list is not empty -> [new_node, head]
            self.head = new_node
        return

    def add_last(self, data):
        """Add a node to the end of the linked list (O(n))"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node # list is empty -> [new_node]
            return
        else:
            current = self.head # list is not empty -> [head, new_node]
            while current.next: # traverse the list until the last node
                current = current.next # move to the next node
            current.next = new_node # add the new node to the end

    def add_at(self, data, index):
        """Add a node at a specific index"""
        pass
    
    def remove(self, data):
        """Remove a node from the linked list"""
        pass

    def remove_last(self):
        """Remove the last node from the linked list"""
        pass

    def remove_at(self, index):
        """Remove a node at a specific index"""
        pass    

    def get(self, data):
        """Get a node from the linked list"""
        pass

    def get_last(self):
        """Get the last node from the linked list"""
        pass

    def get_at(self, index):
        """Get a node at a specific index"""
        pass