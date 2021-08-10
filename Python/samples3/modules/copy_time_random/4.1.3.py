#!/usr/bin/env python3
"""
Текущее время
"""
import time
from datetime import date

today = date.today()
print(today)

print(date(2007, 12, 5))
print(today == date.fromtimestamp(time.time()))

my_birthday = date(today.year, 6, 24)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
print(my_birthday)

time_to_birthday = abs(my_birthday - today)
print(time_to_birthday.days)
