# -*- encoding: utf-8 -*-
"""
Инструкция finally
"""

try:
     raise KeyboardInterrupt
finally:
     print 'Goodbye, world!'
