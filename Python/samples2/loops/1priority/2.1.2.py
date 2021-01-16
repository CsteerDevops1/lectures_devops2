# -*- encoding: utf-8 -*-
"""
Инструкции
"""

a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6

if a == b and c == d and   \
   d == e and f == g:
   print 'olde'                  # backslashes allow continuations

if (a == b and c == d and
    d == e and e == f):
    print 'new'                  # but parentheses usually do too

print "Here" 
