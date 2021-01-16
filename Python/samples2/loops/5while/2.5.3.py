# -*- encoding: utf-8 -*-
"""
Цикл с завершением
"""

y = 10

x = y / 2                          # for some y > 1
while x > 1:
    if y % x == 0:                 # remainder
        print y, 'has factor', x
        break                      # skip else
    x = x-1
else:                              # normal exit
    print y, 'is prime'
