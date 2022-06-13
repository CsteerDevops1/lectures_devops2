#!/usr/bin/env python3

for i in [ (lambda x: x**y) for y in range(10) ] : print(i(2))
for i in ( (lambda x: x**y) for y in range(10) ) : print(i(2))


y = 2
sq = lambda x : x**y
y = 3
cube = lambda x : x**y
sq(2), cube(2)
