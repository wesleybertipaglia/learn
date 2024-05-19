# Regular Expressions or RegEx 
# is a powerful tool for various kinds of string manipulation.
# They are a domain specific language (DSL) 
# that is present as a library in most modern programming languages, not just Python.

import re
text = "Python is a programming language that lets you work quickly and integrate systems more effectively."

# Methods
# match(): Determine if the RE matches at the beginning of the string.
text_match = re.match(r'Python', text)

# search(): Scan through a string, looking for any location where this RE matches.
text_search = re.search(r'language', text)

# findall(): Find all substrings where the RE matches, and returns them as a list.
text_findall = re.findall(r'language', text)

# split(): Split the string into a list where the RE matches.
text_split = re.split(r'language', text)

# sub(): Find all substrings where the RE matches, and replace them with a different string.
text_sub = re.sub(r'language', 'programming language', text)
