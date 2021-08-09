#!/usr/bin/python3
"""
Вставка элементов
"""

a = ["spam", "eggs", 100, 1234]
# Insert some:
a[1:1] = ["bletch", "xyzzy"]
print(a)

a[:0] = a  # Insert (a copy of) itself at the beginning
print(a)
