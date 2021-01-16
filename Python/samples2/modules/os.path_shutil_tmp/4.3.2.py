# -*- encoding: utf-8 -*-
"""
Работа с файлами и каталогами
"""
import shutil
import os

os.mkdir('example')
print 'BEFORE:', os.listdir('example')
shutil.copy('shutil_copy.py', 'example')
print 'AFTER:', os.listdir('example')from shutil import *
from glob import glob

f = open('example.txt', 'wt')
f.write('contents')
f.close()

print 'BEFORE: ', os.listdir('.')
move('example.txt', 'example.out')
print 'AFTER : ', os.listdir('.')