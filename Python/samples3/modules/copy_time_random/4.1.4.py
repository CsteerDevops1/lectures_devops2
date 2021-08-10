#!/usr/bin/env python3
"""
Календарь
"""
import calendar

month = 0o2
year = 2021

month_matrix = calendar.monthcalendar(year, month)

# print out the heading
print(f"{calendar.month_name[month]} {year}\n")

# print out each day in hex; if the day = 0, then leave it blank
for week in month_matrix:
    for day in week:
        if day == 0:
            print("  ", end=' ')
        else:
            print(f"{hex(day)[2:]:>2}", end=' ')
    print()
