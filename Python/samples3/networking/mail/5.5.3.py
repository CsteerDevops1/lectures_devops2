# -*- encoding: utf-8 -*-

"""
Получение почты по протоколу IMAP
"""

import getpass
import imaplib

mailbox = imaplib.IMAP4()
mailbox.login(getpass.getuser(), getpass.getpass())
mailbox.select()
typ, data = mailbox.search(None, "ALL")
for num in data[0].split():
    typ, data = mailbox.fetch(num, "(RFC822)")
    print(f"Message {num}\n{data[0][1]}\n")
mailbox.close()
mailbox.logout()
