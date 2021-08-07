#!/usr/bin/python3
"""
Подсчёт сложных процентов
"""

principal = 1000.0  # starting principal
rate = .05  # interest rate

print("Year %21s" % "Amount on deposit")

for year in range(1, 11):
    amount = principal * (1.0 + rate) ** year
    print("%4d%21.2f" % (year, amount))
