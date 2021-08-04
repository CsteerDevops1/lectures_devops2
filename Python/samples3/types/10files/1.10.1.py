#!/usr/bin/python3
"""
Открытие файла
"""

# open() returns a file object, and is most commonly used with two arguments:
# "open(filename, mode)".

f = open("/tmp/workfile", "w")
print(f)

# Context manager
with open("/tmp/workfile", "w") as f:
    print(f)

# mode can be "r" when the file will only be read,
# "w" for only writing (an existing file with the same name will be erased),
# "a" opens the file for appending; any data written to the file is automatically
#      added to the end.
# "r+" opens the file for both reading and writing.
# The mode argument is optional; "r" will be assumed if it"s omitted.

# On Windows and the Macintosh, "b" appended to the mode opens the file in binary
# mode so there are also modes like "rb", "wb", and "r+b".
