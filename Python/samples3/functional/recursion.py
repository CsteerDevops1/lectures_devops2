#!/usr/bin/env python3

def quicksort(lst):
  "Quicksort over a list-like sequence"
  if len(lst) == 0:
    return lst
  pivot = lst[0]
  pivots = [ x for x in lst if x == pivot ]
  small = quicksort([x for x in lst if x < pivot])
  large = quicksort([x for x in lst if x > pivot])
  return small + pivots + large
