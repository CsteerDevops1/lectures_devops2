#!/usr/bin/python3
"""
Разница между добавлением и расширением
"""

li = ["a", "b", "c"]
li.extend(["d", "e", "f"])
print(li)

print(len(li))

print(li[-1])

li = ["a", "b", "c"]
li.append(["d", "e", "f"])

print(li)

print(len(li))

print(li[-1])
