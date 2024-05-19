# Interfaces
# A way to guarantee that a class will have some methods from a superclass

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area():
        pass

    @abstractmethod
    def get_perimeter():
        pass

class Retangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length * self.width)