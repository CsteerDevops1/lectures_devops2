#!/usr/bin/python3
"""
Конвертация комплексных в вещественные
"""

# The conversion functions to floating point and integer
# (float(), int() and long()) don't work for complex numbers

a = 3.0 + 4.0j

print(a.real)

print(a.imag)

print(abs(a))  # sqrt(a.real**2 + a.imag**2)
