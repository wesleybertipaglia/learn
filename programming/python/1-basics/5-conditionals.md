# Conditionals

## If Statement

The `if` statement is used to execute a block of code only if a condition is true.

```python
if 5 > 2:
    print("Five is greater than two!")
elif 5 == 2:
    print("Five is equal to two!")
else:
    print("Five is less than two!")
```

## Short Hand If

If you have only one statement to execute, you can put it on the same line as the `if` statement.

```python
if 5 > 2: print("Five is greater than two!")
```

## Short Hand If ... Else

If you have only one statement to execute, one for `if`, and one for `else`, you can put it all on the same line.

```python
print("5") if 5 > 2 else print("2")
```
