# -*- encoding: utf-8 -*-
"""
Простейший селектор
"""

a = "first" 
b = "second" 
print 1 and a or b

print 0 and a or b

# evaluated from left to right, so the and is evaluated first. 

# 0 and 'first' evaluates to False, and then 0 or 'second' evaluates to 'second'.
