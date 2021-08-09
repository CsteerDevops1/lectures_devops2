#!/usr/bin/python3
"""
Форматирование
"""

print("%2s %5s %12s" % ('x', 'x**2', 'x**x'))
print("=" * 21)
for x in range(1, 6):
    print("%2d %5d %12d" % (x, x**2, x**x))
