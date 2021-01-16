# -*- encoding: utf-8 -*-
"""
Базовый синтаксис
"""

try:
    num = float(raw_input("\nEnter a number: "))
except(ValueError):
    print "That was not a number!" 
else:
    print "You entered the number", num     
