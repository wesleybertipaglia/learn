# Generator
# A generator is a function that returns an iterator
# It yields values one at a time using the yield keyword

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# instances
fibonacci_gen = fibonacci_sequence()
for i in range(10):  # Print the first 10 Fibonacci numbers
    print(next(fibonacci_gen))
