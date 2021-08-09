#!/usr/bin/env python3
"""
Поверхностное и глубокое копирование
"""
import copy

list_one = [
    {
        "name": "Willie",
        "city": "Providence, RI",
    },
    1,
    "tomato",
    3.0,
]

list_two = list_one[:]
list_two = copy.copy(list_one)
list_three = copy.deepcopy(list_one)

list_one.append("kid")
list_one[0]["city"] = "San Francisco, CA"

print(list_one)
print(list_two)
print(list_three)
