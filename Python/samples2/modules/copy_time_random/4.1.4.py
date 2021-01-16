# -*- encoding: utf-8 -*-
"""
Календарь
"""
import calendar

month = 01
year  = 2020

monthMatrix = calendar.monthcalendar(year, month)

# print out the heading
print "%s %d\n" % (calendar.month_name[month], year)

# print out each day in hex; if the day = 0, then leave it blank
for week in monthMatrix:
    for day in week:
        if day == 0:
           print "  ",
        else:
           print "%2s" % (hex(day)[2:]), 
    print
