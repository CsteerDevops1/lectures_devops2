#!/usr/bin/env python3
"""
Работа с файлами и каталогами
"""
import shutil
import os

os.mkdir("example")
print("BEFORE:", os.listdir("example"))
shutil.copy("4.3.2.py", "example")
print("AFTER:", os.listdir("example"))

with open("example.txt", "wt") as f:
    f.write("contents")

print("BEFORE: ", os.listdir("."))
shutil.move("example.txt", "example.out")
print("AFTER: ", os.listdir("."))
