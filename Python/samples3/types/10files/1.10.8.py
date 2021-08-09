#!/usr/bin/python3
"""
Определение позиции в файле
"""

with open("somefile", "wb") as f:
    f.truncate(1024000)

with open("somefile") as f:
    print(f.read(3))
    print(f.read(2))
    print(f.tell())
