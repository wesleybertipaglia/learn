# Operators

# arithmetic
sum = 1 + 2
sub = 5 - 3
mul = 8 * 5
div = 10 / 2
flo = 11 // 2 # absolute division (discard the decimal part) = 5
mod = 33 % 2 # module (remainder of the division) = 1
exp = 2 ** 3 # exponentiation = 8

# assignment
x = 10  # Assignment
x += 5  # Addition Assignment
x -= 3  # Subtraction Assignment
x *= 2  # Multiplication Assignment
x /= 4  # Division Assignment
x //= 3  # Floor Division Assignment
x %= 2  # Modulus Assignment
x **= 3  # Exponentiation Assignment

# comparison
x, y, z, w, a, b = 1, 2, 3, 4, 5, 6
x == 10
y != 5
z > 3
w < 8
a >= 20
b <= 15

# logical
x and y
a or b
not z

# identity
x is y
a is not b

# membership
fruits = ['apple', 'banana', 'kiwi', 'mango']
'apple' in fruits
'banana' not in fruits

# bitwise
result = 0b1101 & 0b1010  # and
result = 0b1101 | 0b1010 # or
result = 0b1101 ^ 0b1010 # xor (only 1 has to be true)
result = ~0b1101 # not
result = 0b1101 << 2 # left shift
result = 0b1101 >> 2 # right shift