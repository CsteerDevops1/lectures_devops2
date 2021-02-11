#!/usr/bin/env python3

str_str = "abcdef"
str_iter = iter(str_str)
print(str_iter == iter(str_iter))


iter_file = open('/etc/passwd')
print( '__iter__' in dir(iter_file) and '__next__' in dir(iter_file) )

iter_map  = map(lambda x: x+1, range(10))
print( '__iter__' in dir(iter_map)  and '__next__' in dir(iter_map)  )

def count_to_n(n):
  for i in range(n):
    yield i

print( '__iter__' in dir(count_to_n) )
print( '__iter__' in dir(count_to_n(20)) and '__next__' in dir(count_to_n(20)))

lst = [1,2,3]
print( '__iter__' in dir(lst))
print( '__next__' in dir(lst))
li = iter(lst)
print( li == iter(li) )
print( '__iter__' in dir(li) and '__next__' in dir(li) )
