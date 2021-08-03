#!/usr/bin/python3
"""
Конкатенация списков
"""

num_list = [43, -1.23, -2, 6.19e5]
str_list = ["jack", "jumped", "over", "candlestick"]
mixup_list = [4.0, [1, "x"], "beef", -1.9+6j]

print(num_list + mixup_list)
print(str_list + num_list)
