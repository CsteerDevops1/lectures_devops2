#!/usr/bin/python3
"""
Преобразования строк и чисел
"""

print(int("42"), str(42))  # convert from/to string

print(int("42") + 1)  # force addition

print(int("42"), str(42))  # convert from/to string

print("spam" + str(42))  # force concatenation

print(int("5"))
print(int(5.2))
print(int("5.2"))  # ValueError
