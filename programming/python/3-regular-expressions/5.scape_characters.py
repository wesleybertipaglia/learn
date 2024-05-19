# Scape Characters
# Scape characters are used to escape special characters in regular expressions.

import re
text = "Python is a programming language that lets you work quickly and integrate systems more effectively."

# \: Escape special characters
scape_characters = re.findall(r'\.', text)

# \\: Backslash
scape_backslash = re.findall(r'\\', text)

# \a: 
scape_a = re.findall(r'\a', text)

# \b: represents a word boundary, and means "backspace" only inside a character class.
scape_b = re.findall(r'\b', text)

# \f: 
scape_f = re.findall(r'\f', text)

# \n:
scape_n = re.findall(r'\n', text)

# \N:
scape_N = re.findall(r'\N', text)

# \r:
scape_r = re.findall(r'\r', text)

# \t:
scape_t = re.findall(r'\t', text)

# \u: 
scape_u = re.findall(r'\u', text)

# \U:
scape_U = re.findall(r'\U', text)

# \v:
scape_v = re.findall(r'\v', text)

# \x:
scape_x = re.findall(r'\x', text)