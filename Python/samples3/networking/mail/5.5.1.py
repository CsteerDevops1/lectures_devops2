#!/usr/bin/env python3

"""
Отправка почты по протоколу SMTP
"""

import smtplib


def prompt(prompt):
    return input(prompt).strip()


fromaddr = prompt("From: ")
toaddrs = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = f"From: {fromaddr}\r\nTo: {', '.join(toaddrs)}\r\n\r\n"

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is ", len(msg))

server = smtplib.SMTP("localhost")
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
