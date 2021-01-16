# -*- encoding: utf-8 -*-
"""
Присваивание
"""

nudge = 1
wink  = 2
A, B = nudge, wink             # tuple assignment
print A, B                           # like A=nudge; B=wink

nudge = 1
wink  = 2
nudge, wink = wink, nudge      # tuples: swaps values
print nudge, wink                    # like T=nudge; nudge=wink; wink=T
