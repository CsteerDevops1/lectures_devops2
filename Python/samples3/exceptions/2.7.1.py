# -*- encoding: utf-8 -*-
"""
Базовый синтаксис
"""

try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("That was not a number!")
else:
    print(f"You entered the number {num}")   
