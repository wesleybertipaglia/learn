# Conditionals

# If statement
if 5 > 2:
    print("5 is greater than 2")

# If statement with else
if 2 > 5:
    print("2 is greater than 5")
else:
    print("2 is not greater than 5")

# If statement with elif
if 2 > 5:
    print("2 is greater than 5")
elif 2 == 5:
    print("2 is equal to 5")
else:
    print("2 is not greater than 5 and not equal to 5")

# Short hand if
if 5 > 2: print("5 is greater than 2")

# Short hand if with else
print("5 is greater than 2") if 5 > 2 else print("5 is not greater than 2")

# Short hand if with elif
print("5 is greater than 2") if 5 > 2 else print("5 is not greater than 2") if 5 < 2 else print("5 is equal to 2")

# And
if 5 > 2 and 3 > 2:
    print("Both conditions are true")

# Or
if 5 > 2 or 3 < 2:
    print("At least one condition is true")

# Nested if
x = 41
if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20")
else:
    print("Not above ten")

# Pass
if 5 > 2:
    pass
else:
    print("5 is not greater than 2")