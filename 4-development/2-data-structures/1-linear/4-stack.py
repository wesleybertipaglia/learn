# Ordered: Yes
# Mutable: Yes
# Duplicates: Yes
# Indexing: Yes (though typically not used)
# Different Data Types: Yes

class Stack:
    def __init__(self):
        self.items = []
        self.top = None

    # Check if the stack is empty
    def __is_empty(self):
        return self.top == None

    # Get the size of the stack
    def size(self):
        return len(self.items)

    # Print the stack
    def print(self):
        print(self.items)    

    # Push an element onto the stack
    def push(self, item):
        self.items.append(item)
        self.top = item

    # Pop an element from the stack
    def pop(self):
        if self.__is_empty():
            raise IndexError("Cannot pop from an empty stack")
        self.top = self.items[-2] # last element after pop
        return self.items.pop()

    # Peek at the top element of the stack
    def peek(self):
        if self.__is_empty():
            raise IndexError("Cannot peek from an empty stack")
        return self.top

