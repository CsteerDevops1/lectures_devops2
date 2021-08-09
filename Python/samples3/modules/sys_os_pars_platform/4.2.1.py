#!/usr/bin/env python3
"""
Аргументы командной строки
"""
import os
import sys
from calendar import monthcalendar

print("sys.argv[0] =", sys.argv[0])
pathname = os.path.dirname(sys.argv[0])
print("path =", pathname)
print("full path =", os.path.abspath(pathname))

# make sure we have the right number of command line parameters
if len(sys.argv) != 3:
    print("\nSyntax: hexcal month year (where month is 1 - 12)\n")
    sys.exit(1)

# convert the two command line parameters to numerical values
# (they come in as strings)
try:
    month = int(sys.argv[1])
    year = int(sys.argv[2])

    # get the matrix of days and weeks in the month
    month_matrix = monthcalendar(year, month)
    print(month_matrix)

except ValueError as message:
    print("Error:", message)
    sys.exit(2)
