#!/usr/bin/python3
"""
Многострочная строчка
"""

# Continuation lines can be used, with a backslash as the last character on the
# line indicating that the next line is a logical continuation of the line:

hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."

print(hello)
