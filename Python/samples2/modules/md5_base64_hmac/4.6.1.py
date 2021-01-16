# -*- encoding: utf-8 -*-
"""
Вычисление хэша
"""

import hashlib

m = hashlib.md5()
m.update("Nobody inspects")
m.update(" the spammish repetition")
m.digest()

m.digest_size

m.block_size
