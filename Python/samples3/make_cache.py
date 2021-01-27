#!/usr/bin/env python3

def make_cache(function):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return wrapper


@make_cache
def fib(n):
    if n < 2 : return n
    return fib(n-1) + fib(n-2)

