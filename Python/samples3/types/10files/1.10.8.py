#!/usr/bin/python3
"""
Определение позиции в файле
"""

with open(r"c:\text\somefile.txt") as f:
    f.read(3)
    f.read(2)
    f.tell()
