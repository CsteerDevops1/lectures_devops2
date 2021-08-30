#!/usr/bin/env python3
"""
TCP клиент
"""
# https://docs.python.org/3/library/asyncio-protocol.html#tcp-echo-client

import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))