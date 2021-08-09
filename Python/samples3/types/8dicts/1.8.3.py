#!/usr/bin/python3
"""
Конструирование словаря из списков
"""

# dict() constructor builds dictionaries directly from lists of key-value pairs stored
# as tuples.

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print(dict([(x, x ** 2) for x in (2, 4, 6)]))     # use a list comprehension

# When the keys are simple strings, it is sometimes easier to specify pairs using
# keyword arguments:

print(dict(sape=4139, guido=4127, jack=4098))
