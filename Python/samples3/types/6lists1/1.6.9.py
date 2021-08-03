#!/usr/bin/python3
"""
Удаление элемента
"""

li = ["a", "b", "new", "mpilgrim", "z", "example", "new", "two", "elements"]

print(li.remove("z"))  # Does not return a value
print(li)

li.remove("new")
print(li)

x = li.pop()
print(x, li)

x = li.pop(-1)
print(x, li)

x = li.pop(3)
print(x, li)

li.remove("z")  # ValueError
