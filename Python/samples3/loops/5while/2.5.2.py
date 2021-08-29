#!/usr/bin/python3
"""
Прерывание цикла
"""

while 1:
    word = input('Please enter a word: ')
    if not word: 
        break
    print('The word was ' + word)
