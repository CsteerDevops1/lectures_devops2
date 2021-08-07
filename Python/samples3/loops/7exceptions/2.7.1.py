#!/usr/bin/python3
"""
Базовый синтаксис
"""

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)
