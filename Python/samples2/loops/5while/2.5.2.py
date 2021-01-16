# -*- encoding: utf-8 -*-
"""
Прерывание цикла
"""

while 1:
    word = raw_input('Please enter a word: ')
    if not word: 
        break
    print 'The word was ' + word
