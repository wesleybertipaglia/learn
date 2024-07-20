# Loops

## For Loop

The `for` loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. It is often used when you have a piece of code which you want to repeat n number of times.

### For in

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
```

### For range

```python
for x in range(6):
    print(x)
```

## While Loop

The `while` loop is used to execute a block of code as long as a condition is true.

```python
i = 1

while i < 6:
    print(i)
    i += 1
```

## Nested Loops

A nested loop is a loop inside a loop.

```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
```

## Loop Control Statements

Loop control statements change the execution from its normal sequence.

### Break Statement

With the `break` statement we can stop the loop before it has looped through all the items.

```python
for x in fruits:
    print(x)
    if x == "banana":
        break
```

### Continue Statement

With the `continue` statement we can stop the current iteration of the loop, and continue with the next.

```python
for x in fruits:
    if x == "banana":
        continue
    print(x)
```
