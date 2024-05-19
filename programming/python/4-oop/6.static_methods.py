# Static Methods
# Defined using the @staticmethod decorator
# Don't require access to instance variables (self)

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            print("Error: Division by zero.")

# Usage
print(MathOperations.add(5, 3))
print(MathOperations.subtract(10, 4))
print(MathOperations.multiply(2, 6))
print(MathOperations.divide(8, 2))
print(MathOperations.divide(10, 0))