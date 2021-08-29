#!/usr/bin/python3
"""
Динамическая типизация
https://docs.python.org/3/library/typing.html?highlight=typing#the-any-type
"""

x = 0            # x bound to an integer object
print(x)

x = "Hello"      # now it's a string
print(x)

x = [1, 2, 3]    # and now it's a list
print(x)
