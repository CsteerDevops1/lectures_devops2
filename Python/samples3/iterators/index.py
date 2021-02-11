#!/usr/bin/env python3

index = lambda lst,i: next( x for x in enumerate(lst) if x[1] == i)[0]
print(index([3,5,2,22,67,15,15,4],15))
