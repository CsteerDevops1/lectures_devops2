#!/usr/bin/env python3
"""
Сжатие
"""

import glob
import os
import zipfile

# Open the zip file for writing, and write stuff to it

file = zipfile.ZipFile("test.zip", "w")

for name in glob.glob("./*"):
    file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)

file.close()

# open the file again, to see what's in it

file = zipfile.ZipFile("test.zip", "r")

for name in file.namelist():
    data = file.read(name)
    print(name, len(data), repr(data[:10]))

for info in file.infolist():
    print(info.filename, info.date_time, info.file_size, info.compress_size)
