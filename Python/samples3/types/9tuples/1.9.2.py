#!/usr/bin/python3
"""
Присваивание
"""

nudge = 1
wink = 2
a, b = nudge, wink  # tuple assignment
print(a, b)  # like A=nudge; B=wink

nudge = 1
wink = 2
nudge, wink = wink, nudge  # tuples: swaps values
print(nudge, wink)  # like T=nudge; nudge=wink; wink=T
