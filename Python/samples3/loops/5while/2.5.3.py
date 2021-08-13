#!/usr/bin/python3
"""
Цикл с завершением
https://docs.python.org/3/reference/simple_stmts.html#break
"""

y = 10

x = y // 2                          # for some y > 1
print(x)
while x > 1:
    if y % x == 0:                 # remainder
        print(y, 'has factor', x)
        break                      # skip else
    x = x - 1                      # x -= 1
else:                              # normal exit
    print(y, 'is prime')
