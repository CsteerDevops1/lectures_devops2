# -*- encoding: utf-8 -*-
"""
Базовый синтаксис
"""

try:
    num = 1/float(raw_input("\nEnter a number: "))
except(ValueError,KeyboardInterrupt,ZeroDivisionError,EOFError), exc:
    print exc 
else:
    print "You entered the number", num     
