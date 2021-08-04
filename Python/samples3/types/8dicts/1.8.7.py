#!/usr/bin/python3
"""
Изменение, добавление и удаление значений
"""

d2 = {"spam": 2, "ham": 1, "eggs": 3}  # make a dictionary

print(d2)  # order is scrambled

d2["ham"] = ["grill", "bake", "fry"]  # change entry

del d2["eggs"]  # delete entry

d2["brunch"] = "Bacon"  # add new entry

print(d2)
