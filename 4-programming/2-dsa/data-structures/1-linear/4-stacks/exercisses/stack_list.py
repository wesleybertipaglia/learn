class Stack:
    """
    Stack data structure implemented using a list
    """
    def __init__(self):
        self.items = []
        self.top = None

    def __is_empty(self):
        """
        return true if the stack is empty
        """
        return self.top == None
    
    def size(self):
        """
        return the stack size
        """
        return len(self.items)
    
    def print(self):
        """
        print the stack
        """
        print(self.items)
    
    def push(self, item):
        """
        push an item to stack and return it
        """
        self.items.append(item)
        self.top = item
        return self.top

    def pop(self):
        """
        pop the last item from stack and return it
        """
        if self.__is_empty():
            raise IndexError("Cannot pop from an empty stack")
        self.top = self.items[-2]
        return self.items.pop()
    
    def peek(self):
        """
        return the top item
        """
        if self.__is_empty():
            raise IndexError("Cannot peek from an empty stack")
        return self.top
