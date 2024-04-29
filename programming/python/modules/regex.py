import re

lorem = """Lorem ipsum is placeholder text commonly used in the graphic, 
    print, and publishing industries for previewing layouts and visual mockups."""

pattern = "ipsum"

# Search for a pattern in a lorem and return the first match
re.search(pattern, lorem, flags=0)

# Match a pattern at the beginning of a lorem
re.match(pattern, lorem, flags=0)

# Find all occurrences of a pattern in a lorem and return them as a list of match objects
re.findall(pattern, lorem, flags=0)

# Find all occurrences of a pattern in a lorem and return them as an iterator of match objects
re.finditer(pattern, lorem, flags=0)

# Split a lorem by occurrences of a pattern
re.split(pattern, lorem, maxsplit=0, flags=0)

# Replace occurrences of a pattern in a lorem with a replacement lorem
re.sub(pattern, "hello", lorem, count=0, flags=0)

# Compile a regular expression pattern into a regex object for later use
re.compile(pattern, flags=0)

# Escape special characters in a lorem to be treated as literals in a regular expression
re.escape(lorem)
