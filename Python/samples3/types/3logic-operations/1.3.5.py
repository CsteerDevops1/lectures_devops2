#!/usr/bin/python3
"""
Побитовое ИЛИ
"""
from operator import or_

x = 1  # 0001

a = x | 2  # bitwise OR: 0011

b = or_(x, 2)

print(a, b)
