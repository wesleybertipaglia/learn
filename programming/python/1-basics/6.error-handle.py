# Error handling

# try, except
x = 10
try:
    print(x)
except:
    print("An exception occurred")

# try, except with specific exception
try:
    print(x)
except NameError:
    print("Variable x is not defined")

# try, except with specific exception and else
try:
    print("Hello")
except NameError:
    print("Variable x is not defined")
else:
    print("Nothing went wrong")

# try, except with specific exception, else and finally
try:
    print(x)
except NameError:
    print("Variable x is not defined")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")