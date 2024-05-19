# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:

import re
text = "Python is a programming language that lets you work quickly and integrate systems more effectively."

# [arn]: Returns a match where one of the specified characters (a, r, or n) are present
match_arn = re.findall(r'[arn]', text)

# [a-n]: Returns a match for any lower case character, alphabetically between a and n
match_a_n = re.findall(r'[a-n]', text)

# [^arn]: Returns a match for any character EXCEPT a, r, and n
match_not_arn = re.findall(r'[^arn]', text)

# [0123]: Returns a match where any of the specified digits (0, 1, 2, or 3) are present
match_0123 = re.findall(r'[0123]', text)

# [0-9]: Returns a match for any digit between 0 and 9
match_0_9 = re.findall(r'[0-9]', text)

# [0-5][0-9]: Returns a match for any two-digit numbers from 00 and 59
match_0_5_0_9 = re.findall(r'[0-5][0-9]', text)

# [a-z]: Returns a match for any lowercase alphabetically character between a and z
match_a_z = re.findall(r'[a-z]', text)

# [A-Z]: Returns a match for any uppercase alphabetically character between A and Z
match_A_Z = re.findall(r'[A-Z]', text)

# [a-zA-Z]: Returns a match for any character alphabetically between a and z, lower case OR upper case
match_a_z_A_Z = re.findall(r'[a-zA-Z]', text)

# [+] : In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
match_plus = re.findall(r'[+]', text)