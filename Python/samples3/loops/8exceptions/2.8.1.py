#!/usr/bin/python3
"""
Деление на ноль
https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
"""

try:
    1 / 0
except ZeroDivisionError:
    print("caught divide-by-0 attempt")
