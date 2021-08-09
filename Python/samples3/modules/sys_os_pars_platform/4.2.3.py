#!/usr/bin/env python3
"""
Переменные окружения
"""
import os

os.environ["USER"] = "Mel"
os.popen("python echoenv.py").read()

print(os.environ.keys())

os.environ["TEMP"]

os.environ["TEMP"] = r"c:\temp"
print(os.environ["TEMP"])
