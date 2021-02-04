# -*- encoding: utf-8 -*-
"""
Обратный DNS клиент
"""
import sys, socket

try:
    result = socket.gethostbyaddr("66.249.71.15")
    print "Primary hostname:" 
    print "  " + result[0]

    # Display the list of available addresses that is also returned
    print "\nAddresses:" 
    for item in result[2]:
        print "  " + item
except socket.herror, e:
    print "Couldn't look up name:", e