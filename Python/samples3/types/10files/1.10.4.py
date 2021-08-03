#!/usr/bin/python3
"""
Чтение строк из файла
"""

f = open("filename")
for line in f.readlines():
    print("Line: " + line)
