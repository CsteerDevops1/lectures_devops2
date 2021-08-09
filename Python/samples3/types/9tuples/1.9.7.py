#!/usr/bin/python3
"""
Распаковка кортежей (или любых последовательностей)
"""

p = (4, 5)
x, y = p

data = ('ACME', 50, 91.1, (2012, 12, 21))
name, shares, price, date = data

first, *middle, last = (1, 1, 2, 3, 5, 8, 13)
print(first, last, middle)

line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir)

x, y, z = p  # ValueError (expected 3, got 2)
