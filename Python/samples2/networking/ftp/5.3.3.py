# -*- encoding: utf-8 -*-
"""
Закачка файла на сервер
"""

import ftplib
ftp = ftblib.FTP("ftp.yourServer.com")
ftp.login("username", "password")
filename = "index.html" 
ftp.storlines("STOR " + filename, open(filename))
filename="app.exe" 
ftp.storbinary("STOR " + filename, open(filename, "rb"), 1024)
ftp.quit()