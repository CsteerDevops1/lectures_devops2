#!/usr/bin/python3
"""
Объединение словарей
"""

c = {"cold": "coke", "hot": "coffee"}
d = {"spam": 1, "eggs": 2, "cheese": 3}
e = {"cheese": "cheddar", "aardvark": "Ethel"}

d.update(e)  # Modifies d in-place
print(d)

cd = {**c, **d}  # Unpacking. Not easily discoverable
print(cd)


def merge_dicts(d1, d2):
    res = {}

    for k, v in d1.items():
        res[k] = v

    for k, v in d2.items():
        res[k] = v

    return res


merged = merge_dicts(c, e)
print(merged)

# Python 3.9
ce = c | e  # Return a new dict
c |= e  # In-place

print(ce)
print(c)
