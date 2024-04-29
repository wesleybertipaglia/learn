# Iterator
# An iterator allows iterating over its elements one at a time
# by defining __iter__ and __next__ methods
# __iter__: Returns the iterator object itself
# __next__: Returns the next item in the sequence

class my_iterator():
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.counter = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter += 1
        if self.counter < len(self.nums):
            return self.nums[self.counter]
        else:
            raise StopIteration
        
first_iterator = my_iterator([5, 43, 4, 3, 7, 2, 1, 9, 34])
for i in first_iterator:
    print(i)