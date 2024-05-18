# Loops

# while loop
i = 0
while i < 10:
    if i == 5:
        break # stop the loop
    if i == 2:
        i += 1
        continue # stop the current iteration
    print(i)
    i += 1

# for loop (in)
fruits = ['apple', 'banana', 'kwi', 'coconut']

for fruit in fruits:
    if fruit == "banana":
        break # break the entry loop
    if fruit == "coconut":
        continue # skip the current interation
    print(fruit)

# for loop (in range)
for x in range(10):
    print(x)

# for loop (in range with start and end)
for x in range(2, 10):
    print(x)

# for loop (in range with start, end and step)
for x in range(2, 10, 2):
    print(x)
