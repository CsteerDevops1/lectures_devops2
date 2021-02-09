# -*- encoding: utf-8 -*-
"""
Ошибка использования типа
"""

value = print

print(f'{repr(value)} is ', end='')

try:
    value + 0
except TypeError:
    # not a number, maybe a string, Unicode, UserString...?
    try:
        value + ''
    except TypeError:
        print("neither a number nor a string")
    else:
        print("a string or string-like value")
else:
    print("a number of some kind" )
