# -*- encoding: utf-8 -*-
"""
Сравнение текстов
"""
import sys
from difflib import get_close_matches
get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])

import keyword
get_close_matches('wheel', keyword.kwlist)

get_close_matches('apple', keyword.kwlist)

get_close_matches('accept', keyword.kwlist)

text1 = """ 
Lavender's blue,
Diddle diddle,
Lavender's green,
When I am king,
Diddle diddle,
You shall be queen.
""" 

text2 = u""" 
Lavender's blue,
Lavender's green,
When I am king,
You shall be queen.
""" 

import difflib
for line in difflib.context_diff(text1, text2, fromfile='text1', tofile='text2'):
    sys.stdout.write(line)  
