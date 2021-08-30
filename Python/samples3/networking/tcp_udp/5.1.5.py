#!/usr/bin/env python3
"""
UDP клиент
"""
# https://docs.python.org/3/library/asyncio-protocol.html#udp-echo-client

import socket, sys, time

host = sys.argv[1]
textport = "51423"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)

s.connect((host, port))
print("Enter data to transmit: ")
data = sys.stdin.readline().strip()
s.sendall(bytes(data, 'utf-8'))
s.shutdown(1)
print("Looking for replies; press Ctrl-C or Ctrl-Break to stop.")
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    print("Received: %s" % buf)