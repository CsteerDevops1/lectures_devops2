#!/usr/bin/python3
"""
Инструкция finally
https://docs.python.org/3/reference/compound_stmts.html#finally
"""

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
