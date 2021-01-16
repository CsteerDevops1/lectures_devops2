# -*- encoding: utf-8 -*-
"""
Деление на ноль
"""

try: 1/0
except ZeroDivisionError: 
   print "caught divide-by-0 attempt" 
