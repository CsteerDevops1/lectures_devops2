#!/usr/bin/python3
"""
Побитовое И
"""
from operator import and_

x = 1  # 0001

a = x & 1  # bitwise AND: 0001

b = and_(x, 1)

print(a, b)
