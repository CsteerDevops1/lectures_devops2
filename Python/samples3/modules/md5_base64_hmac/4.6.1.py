#!/usr/bin/env python3
"""
Вычисление хэша
"""

import hashlib

m = hashlib.md5()
# Feeding string objects into update() is not supported, as hashes work on bytes, not on characters.
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.digest())

print(m.digest_size)

print(m.block_size)
