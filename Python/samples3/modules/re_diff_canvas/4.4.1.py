#!/usr/bin/env python3

"""
Сравнение текстов
"""

import keyword
import sys
from difflib import context_diff, get_close_matches

print(get_close_matches("appel", ["ape", "apple", "peach", "puppy"]))

print(get_close_matches("wheel", keyword.kwlist))

print(get_close_matches("apple", keyword.kwlist))

print(get_close_matches("accept", keyword.kwlist))

text1 = """
Lavender's blue,
Diddle diddle,
Lavender's green,
When I am king,
Diddle diddle,
You shall be queen.
"""

text2 = """
Lavender's blue,
Lavender's green,
When I am king,
You shall be queen.
"""

for line in context_diff(text1, text2, fromfile="text1", tofile="text2"):
    sys.stdout.write(line)
