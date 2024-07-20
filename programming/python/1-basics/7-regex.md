# Regular Expressions

Regular expressions are a powerful tool for pattern matching and text processing. They are supported in many programming languages and tools, including Python.

In Python, regular expressions are available through the `re` module. The `re` module provides functions for working with regular expressions, such as searching for patterns, replacing patterns, and splitting text based on patterns.

## Basic Patterns

A regular expression is a sequence of characters that defines a search pattern. Here are some basic patterns:

- `a`, `X`, `9`: Ordinary characters match themselves.
- `.`: A period matches any single character except a newline.
- `^`: A caret matches the start of a string.
- `$`: A dollar sign matches the end of a string.
- `|`: A vertical bar separates alternatives.
- `()`: Parentheses are used to group characters.
- `[]`: Square brackets are used to indicate a set of characters.
- `*`: An asterisk matches zero or more repetitions.
- `+`: A plus sign matches one or more repetitions.
- `?`: A question mark matches zero or one repetition.
- `{n}`: Matches exactly `n` repetitions.
- `{n,}`: Matches `n` or more repetitions.
- `{n,m}`: Matches at least `n` and at most `m` repetitions.

## Using Regular Expressions

To use regular expressions in Python, you need to import the `re` module. Here is an example of searching for a pattern in a string:

```python
import re

txt = "The rain in Spain"

# Search for the pattern "ai" in the text
x = re.search("ai", txt) 

if x:
    print("Pattern found")
else:
    print("Pattern not found")
```
