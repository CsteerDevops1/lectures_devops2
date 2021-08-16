#!/usr/bin/python3
"""
Базовый синтаксис
https://docs.python.org/3/library/exceptions.html#ValueError
"""

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)
