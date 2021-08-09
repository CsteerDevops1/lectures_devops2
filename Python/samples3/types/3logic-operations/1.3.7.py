#!/usr/bin/python3
"""
Побитовый сдвиг
"""
from operator import lshift

x = 1  # 0001

a = x << 2  # shift left 2 bits: 0100

b = lshift(x, 2)

print(a, b)
