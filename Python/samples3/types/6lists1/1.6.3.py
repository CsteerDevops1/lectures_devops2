#!/usr/bin/python3
"""
Добавление элементов
"""

scores = ["1", "2", "3"]

# add a score
score = int(input("What score did you get?: "))
scores.append(score)

# list high-score table
for score in scores:
    print(score)
