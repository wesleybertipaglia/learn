class Queue:
    """
    Queue data structure implemented using a list.
    """
    def __init__(self):
        self.items = []

    def __is_empty(self):
        """
        Checks if the queue is empty.
        """
        return len(self.items) == 0
    
    def print(self):
        """
        Prints the queue elements.
        """
        print("QUEUE:", self.items)

    def peek(self):
        """
        Returns the first element without removing it.
        """
        if self.__is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def rear(self):
        """
        Returns the last element without removing it.
        """
        if self.__is_empty():
            raise IndexError("Rear from an empty queue")
        return self.items[-1]

    def enqueue(self, value):
        """
        Add an element at the end of the queue, and return it.
        """
        self.items.append(value)
        return self.items[-1]

    def dequeue(self):
        """
        Remove the first element of the queue, and return it.
        """
        if self.__is_empty():
            raise IndexError("Rear from an empty queue")
        return self.items.pop(0)
