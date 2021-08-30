#!/usr/bin/env python3
"""
UDP эхо-сервер
"""
# https://docs.python.org/3/library/asyncio-protocol.html#udp-echo-server

import socket, traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while 1:
    try:
        message, address = s.recvfrom(8192)
        print("Got data from", address)
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()