# -*- encoding: utf-8 -*-
"""
Постоянное хранилище языковых объектов
"""
import shelve

d = shelve.open(filename) # open -- file may get suffix added by low-level library

d[key] = data   # store data at key (overwrites old data if using an existing key)
data = d[key]   # retrieve a COPY of data at key (raise KeyError if no such key)
del d[key]      # delete data stored at key (raises KeyError if no such key)
flag = d.has_key(key)   # true if the key exists
klist = d.keys() # a list of all existing keys (slow!)

# as d was opened WITHOUT writeback=True, beware:
d['xx'] = range(4)  # this works as expected, but...
d['xx'].append(5)   # *this doesn't!* -- d['xx'] is STILL range(4)!

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']      # extracts the copy
temp.append(5)      # mutates the copy
d['xx'] = temp      # stores the copy right back, to persist it

d=shelve.open(filename,writeback=True) 
d['xx'].append(5)

d.close()       # close it
