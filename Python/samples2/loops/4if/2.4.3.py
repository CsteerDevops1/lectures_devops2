# -*- encoding: utf-8 -*-
"""
Стандартный селектор
"""

choice = 'ham'
print {'spam':  1.25,         # a dictionary-based 'switch'
       'ham':   1.99,         # use has_key() or get() for default
       'eggs':  0.99,
        'bacon': 1.10}[choice]

if choice == 'spam':
     print 1.25
elif choice == 'ham':
     print 1.99
elif choice == 'eggs':
     print 0.99
elif choice == 'bacon':
     print 1.10
else:
     print 'Bad choice'
