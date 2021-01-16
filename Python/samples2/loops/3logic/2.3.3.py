# -*- encoding: utf-8 -*-
"""
Использование логических операций
"""

t, f = 1, 0
x, y = 88, 99

a = (t and x) or y           # if true, x
print a

a = (f and x) or y           # if false, y
print a

print ((t and [x]) or [y])[0]     # if true, x

print ((f and [x]) or [y])[0]     # if false, y

print (t and f) or y              # fails: f is false, skipped

print ((t and [f]) or [y])[0]     # works: f returned anyhow
