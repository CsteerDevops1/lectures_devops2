# -*- encoding: utf-8 -*-
"""
Текущее время
"""
import time
from datetime import date

today = date.today()
today
datetime.date(2007, 12, 5)
today == date.fromtimestamp(time.time())

my_birthday = date(today.year, 6, 24)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
my_birthday
datetime.date(2008, 6, 24)
time_to_birthday = abs(my_birthday - today)
time_to_birthday.days