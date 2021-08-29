#!/usr/bin/env python3
"""
Получение файла с сервера
"""
from ftplib import FTP

ftp = FTP('127.0.0.1', 'book', 'bookpw')
f = open('MyPycFile.pyc', 'wb')
ftp.set_pasv(1)
ftp.set_debuglevel(1)
ftp.retrbinary('RETR AutoIndent.pyc', f.write)
