# -*- encoding: utf-8 -*-
"""
Чтение и запись CSV формата
"""
import csv

reader = csv.reader(open("some.csv", "rb"))
for row in reader:
    print row

#Reading a file with an alternate format:

import csv
reader = csv.reader(open("passwd", "rb"), delimiter=':', quoting=csv.QUOTE_NONE)
for row in reader:
    print row

import csv
writer = csv.writer(open("some.csv", "wb"))
writer.writerows(someiterable)
