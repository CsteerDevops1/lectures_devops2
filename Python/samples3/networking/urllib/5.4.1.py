#!/usr/bin/env python3

"""
Запрос к серверу, чтение заголовков ответа
"""

import sys
import urllib.error
import urllib.parse
import urllib.request

req = urllib.request.Request(sys.argv[1])

try:
    fd = urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print("Error retrieving data:", e)
    sys.exit(1)

print("Retrieved", fd.geturl())
info = fd.info()
for key, value in info.items():
    print(f"{key} = {value}")
