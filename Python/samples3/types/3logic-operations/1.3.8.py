#!/usr/bin/python3
"""
Побитовое исключающее ИЛИ
"""

from operator import xor

x = 15  # 1111

print(x ^ 3)
print(xor(x, 3))
