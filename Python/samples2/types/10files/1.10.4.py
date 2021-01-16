# -*- encoding: utf-8 -*-
"""
Чтение строк из файла
"""

f = open("filename")
for line in f.readlines():
    print "Line: " + line
