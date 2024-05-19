# Metacharacters
# metacharacters are characters with a special meaning:

import re
text = "Python is a programming language that lets you work quickly and integrate systems more effectively."

# . (dot): Matches any character except newline.
match_dot = re.findall(r'.', text)

# |: Either or
match_or = re.findall(r'Python|language', text)

# /: Escape special characters
match_escape = re.findall(r'\.', text)

# ^: Matches the start of the string.
match_start = re.findall(r'^Python', text)

# $: Matches the end of the string.
match_end = re.findall(r'effectively.$', text)

# *: Matches 0 or more occurrences
match_star = re.findall(r'Py*', text)

# +: Matches 1 or more occurrences
match_plus = re.findall(r'Py+', text)

# ?: Matches 0 or 1 occurrences
match_question = re.findall(r'Py?', text)

# *?, +?, ??: Non-greedy match
match_non_greedy = re.findall(r'Py*', text)

# {n}: Exactly n repetitions
match_n = re.findall(r'Py{2}', text)

# {n,m}: From n to m repetitions
match_n_m = re.findall(r'Py{1,2}', text)

# {n,}: At least n repetitions
match_n_ = re.findall(r'Py{1,}', text)

# {,n}: At most n repetitions
match_n_ = re.findall(r'Py{,2}', text)

# []: A set of characters
match_set = re.findall(r'[a-z]', text)

# (): Capture and group
match_group = re.findall(r'(Python)', text)