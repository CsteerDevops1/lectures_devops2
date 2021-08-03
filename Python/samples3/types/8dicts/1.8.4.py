#!/usr/bin/python3
"""
Доступ к элементам словаря
"""

params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
print(list(params.keys()))

print(list(params.values()))

print(list(params.items()))
