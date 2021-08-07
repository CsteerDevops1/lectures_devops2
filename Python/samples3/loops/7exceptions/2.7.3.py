#!/usr/bin/python3
"""
Инструкция finally
"""

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
