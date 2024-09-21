class Node:
    """
    Node list
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    Stack data structure implemented using a linked list
    """

    def __init__(self):
        self.top = None

    def __is_empty(self):
        """
        Return True if the stack is empty.
        """
        return self.top == None
    
    def size(self):
        """
        Return the number of elements in the stack.
        """
        count = 0
        current = self.top
        while current.next:
            count += 1
            current = current.next
        return count

    def print(self):
        """
        Print the stack elements.
        """
        current = self.top
        print("STACK: ")
        while current.next:
            print(current.value, end=" -> ")
            current = current.next
        print("None")        
    
    def peek(self):
        """
        Return the top element without removing it.
        """
        if self.__is_empty():
            return None
        return self.top.value

    def push(self, value):
        """
        Push an item to the stack and return it.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        return self.top.value
    
    def pop(self):
        """
        Pop the top item from the stack and return it.
        If the stack is empty, return None.
        """
        if self.__is_empty():
            raise IndexError("Cannot pop from an empty stack")
        temp_node = self.top
        self.top = temp_node.next
        return temp_node.value
