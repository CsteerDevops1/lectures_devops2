#!/usr/bin/python3
"""
Индексы и операции со словарём
"""

# Dictionaries are indexed by keys, which can be any immutable type;
# strings and numbers can always be keys.

# Tuples can be used as keys if they contain only strings, numbers, or tuples;
# if a tuple contains any mutable object either directly or indirectly,
# it cannot be used as a key.

# You can"t use lists as keys, since lists can be modified.

# a dictionary is an unordered set of key: value pairs, with the requirement that the
# keys are unique (within one dictionary).

tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)

print(tel["jack"])

del tel["sape"]
tel["irv"] = 4127
print(tel)

list(tel.keys())

print("guido" in tel)

print("guido" in tel)
