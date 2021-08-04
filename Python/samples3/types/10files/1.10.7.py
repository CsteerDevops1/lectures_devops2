#!/usr/bin/python3
"""
Запись строк в файл
"""

with open(r"c:\text\somefile.txt") as f:
    lines = f.readlines()

lines[1] = "isn't a\n"

with open(r"c:\text\somefile.txt", "w") as f:
    f.writelines(lines)
