# -*- encoding: utf-8 -*-
"""
Получение файла с сервера
"""

ftp = ftplib.FTP('127.0.0.1', 'book', 'bookpw')
f = open("MyPycFile.pyc", "wb")
ftp.set_pasv(1)
ftp.set_debuglevel(1)
ftp.retrbinary("RETR AutoIndent.pyc", f.write)