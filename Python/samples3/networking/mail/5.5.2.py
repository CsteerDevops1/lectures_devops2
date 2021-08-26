#!/usr/bin/env python3

"""
Получение почты по протоколу POP3
"""

import getpass
import poplib

mailbox = poplib.POP3("localhost")
mailbox.user(getpass.getuser())
mailbox.pass_(getpass.getpass())
num_messages = len(mailbox.list()[1])

for i in range(num_messages):
    for j in mailbox.retr(i + 1)[1]:
        print(j)
