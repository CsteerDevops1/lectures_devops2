#!/usr/bin/env python3

"""
Запрос к серверу, чтение данных
"""

import socket
import sys
import urllib.error
import urllib.parse
import urllib.request

req = urllib.request.Request(sys.argv[1])

try:
    fd = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print("Error retrieving data:", e)
    print("Server errror document follows:\n")
    print(e.read())
    sys.exit(1)
except urllib.error.URLError as e:
    print("Error retrieving data:", e)
    sys.exit(2)

print("Retrieved", fd.geturl())

bytesread = 0

while 1:
    try:
        data = fd.read(1024)
    except socket.error as e:
        print("Error reading data:", e)
        sys.exit(3)

    if not len(data):
        break
    bytesread += len(data)
    sys.stdout.write(data)

if "Content-Length" in fd.info() and \
   int(fd.info()["Content-Length"]) != int(bytesread):
    print(f"""Expected a document of size {int(fd.info()["Content-Length"])},\
        but read {bytesread} bytes""")

    sys.exit(4)
