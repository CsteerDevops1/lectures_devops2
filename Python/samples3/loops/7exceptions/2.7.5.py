#!/usr/bin/python3
"""
Базовый синтаксис
"""

try:
    num = 1/float(input("\nEnter a number: "))
except (ValueError, KeyboardInterrupt, ZeroDivisionError, EOFError) as exc:
    print(exc)
else:
    print("You entered the number", num)
