import random

fruits = ["apple", "banana", "cherry"]

# Generate a random float between 0.0 and 1.0
random.random()

# Generate a random integer within a specified range
random.randint(1, 10)

# Generate a random integer within a specified range with a step
random.randrange(1, 100)

# Randomly shuffle a sequence in-place
random.shuffle(fruits)

# Choose a random element from a sequence
random.choice(fruits)

# Choose multiple random elements from a sequence without replacement
random.sample(fruits, k=2)

# Choose multiple random elements from a sequence with replacement
random.choices(fruits, weights=None, cum_weights=None, k=2)