# Decorators
# decorators: are methods that can perform actions before and after a method execution
# wraps: preserve the metadata of the original function

from functools import wraps

def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result.upper())
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

greet('Wesley')
print('function name: ', greet.__name__)