#!/usr/bin/env python3
"""
Рабочий каталог и путь поиска модулей
"""
import os
import sys

print("my os.getcwd =>", os.getcwd())
print("my sys.path  =>", sys.path[:6])

if "linux" in sys.platform:
    sys.path.append(r"/home/user/python/lib")

if "win32" in sys.platform:
    sys.path.append(r"C:\python26")
