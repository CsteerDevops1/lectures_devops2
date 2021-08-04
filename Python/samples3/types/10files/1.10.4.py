#!/usr/bin/python3
"""
Чтение строк из файла
"""

with open("filename") as f:
    for line in f:
        print("Line: " + line)
