# -*- encoding: utf-8 -*-
"""
Возбуждение исключения
"""

def err():
    raise IndexError

def aFunction():
    try:
        err()
    except IndexError:
        print 'caught an index error!'
    else:
        print 'no error caught...'

if __name__ == '__main__': 
    aFunction()
