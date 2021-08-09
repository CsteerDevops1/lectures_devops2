#!/usr/bin/python3
"""
Определение
"""

t = ()
print(t)
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

singleton = 'hello',  # <-- note trailing comma
print(len(singleton))
print(singleton)
