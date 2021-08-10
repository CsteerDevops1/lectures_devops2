#!/usr/bin/env python3
"""
Чтение и запись CSV формата
"""
import csv

with open("some.csv") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# Reading a file with an alternate format:

with open("passwd", "r") as passwd_file:
    reader = csv.reader(passwd_file, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

someiterable = [1, 2, 3, 4, 5, 6]
with open("some.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(someiterable)
