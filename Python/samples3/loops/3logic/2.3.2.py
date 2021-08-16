#!/usr/bin/python3
"""
Логическое ИЛИ
https://docs.python.org/3/library/stdtypes.html?highlight=bitwise
"""

print('a' or 'b')
print('' or 'b')
print('' or [] or {})


def side_fx():
     print("in sidefx()")
     return 1


print('a' or side_fx())
