#!/usr/bin/python3
"""
Использование функции range()
"""

from math import sqrt

for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
