#!/usr/bin/env python3
"""
Интервалы времени
"""
from datetime import timedelta

year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)  # adds up to 365 days
print(year == another_year)

ten_years = 10 * year
print(ten_years, ten_years.days // 365)

nine_years = ten_years - year
print(nine_years, nine_years.days // 365)

three_years = nine_years // 3
print(three_years, three_years.days // 365)

print(abs(three_years - ten_years) == 2 * three_years + year)
