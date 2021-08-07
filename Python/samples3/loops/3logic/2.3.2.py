#!/usr/bin/python3
"""
Логическое ИЛИ
"""

print('a' or 'b')
print('' or 'b')
print('' or [] or {})


def side_fx():
     print("in sidefx()")
     return 1


print('a' or side_fx())
