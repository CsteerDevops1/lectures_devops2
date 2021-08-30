#!/usr/bin/env python3
"""
TCP эхо-сервер
"""
# https://docs.python.org/3/library/asyncio-protocol.html#tcp-echo-server

import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()