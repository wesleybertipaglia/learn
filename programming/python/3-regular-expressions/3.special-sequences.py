# Special Sequences
# special sequences are a "\" followed by one of the characters in the list below, and has a special meaning:

import re
text = "Python is a programming language that lets you work quickly and integrate systems more effectively."

# \A: Returns a match if the specified characters are at the beginning of the string.
match_A = re.findall(r'\APython', text)

# \b: Returns a match where the specified characters are at the beginning or at the end of a word.
match_b = re.findall(r'language\b', text)

# \B: Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word.
match_B = re.findall(r'\Blanguage', text)

# \d: Returns a match where the string contains digits (numbers from 0-9).
match_d = re.findall(r'\d', text)

# \D: Returns a match where the string DOES NOT contain digits.
match_D = re.findall(r'\D', text)

# \s: Returns a match where the string contains a white space character.
match_s = re.findall(r'\s', text)

# \S: Returns a match where the string DOES NOT contain a white space character.
match_S = re.findall(r'\S', text)

# \w: Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character).
match_w = re.findall(r'\w', text)

# \W: Returns a match where the string DOES NOT contain any word characters.
match_W = re.findall(r'\W', text)

# \Z: Returns a match if the specified characters are at the end of the string.
match_Z = re.findall(r'effectively\Z', text)