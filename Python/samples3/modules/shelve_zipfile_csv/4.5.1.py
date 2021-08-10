
#!/usr/bin/env python3
"""
Постоянное хранилище языковых объектов
"""

import shelve

filename = "shelve"
key = "salad"
data = [
    "tomatoes",
    "cucumbers",
    "onion",
    "feta cheese",
    "olives",
]

d = shelve.open(filename)  # open -- file may get suffix added by low-level library

d[key] = data              # store data at key (overwrites old data if ising an existing key)

data = d[key]              # retrieve a COPY of data at key (raise KeyError if no such key)

del d[key]                 # delete data stored at key (raises KeyError if no such key)

flag = key in d            # true if the key exists
klist = list(d.keys())     # a list of all existing keys (slow!)

# as d was opened WITHOUT writeback=True, beware:
d["xx"] = [0, 1, 2]        # this works as expected, but...
d["xx"].append(3)          # *this doesn"t!* -- d["xx"] is STILL [0, 1, 2]!

# having opened d without writeback=True, you need to code carefully:
temp = d["xx"]      # extracts the copy
temp.append(5)      # mutates the copy
d["xx"] = temp      # stores the copy right back, to persist it

# or, d=shelve.open(filename,writeback=True) would let you just code
# d["xx"].append(5) and have it work as expected, BUT it would also
# consume more memory and make the d.close() operation slower.

d.close()                  # close it
