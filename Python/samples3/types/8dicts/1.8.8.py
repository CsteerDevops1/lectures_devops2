#!/usr/bin/python3
"""
Копирование словаря
"""

x = {"username": "admin", "machines": ["foo", "bar", "baz"]}
y = x.copy()
y["username"] = "mlh"
y["machines"].remove("bar")
print(y)

print(x)
