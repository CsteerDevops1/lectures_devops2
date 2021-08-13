#!/usr/bin/python3
"""
Вложенная обработка
https://docs.python.org/3/tutorial/errors.html
"""

try:
    try:
        1 / 0
    except:
        print("caught an exception")
except ZeroDivisionError:
    print("caught divide-by-0 attempt")
