#!/usr/bin/env python3
"""
Обратный DNS клиент
"""
#https://docs.python.org/3/library/socket.html#socket.gethostbyaddr

import socket

try:
    result = socket.gethostbyaddr("66.249.71.15")
    print("Primary hostname:", end=' ')
    print(result[0])

    # Display the list of available addresses that is also returned
    print("\nAddresses:", end=' ')
    for item in result[2]:
        print(item)
except socket.herror as e:
    print("Couldn't look up name:", e)