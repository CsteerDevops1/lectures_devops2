#!/usr/bin/python3
"""
Возбуждение исключения
https://docs.python.org/3/reference/simple_stmts.html#raise
"""


def err():
    raise IndexError


def aFunction():
    try:
        err()
    except IndexError:
        print('caught an index error!')
    else:
        print('no error caught...')


if __name__ == '__main__': 
    aFunction()
