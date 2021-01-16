# -*- encoding: utf-8 -*-
"""
Запись строк в файл
"""

f = open(r'c:\text\somefile.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n" 
f = open(r'c:\text\somefile.txt', 'w')
f.writelines(lines)
f.close()
