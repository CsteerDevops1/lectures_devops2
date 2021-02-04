#!/usr/bin/env python3

def fact(n):
#  print(f'calculating - {n}')
  if n == 0:
    return 1
  return n*fact(n-1)
