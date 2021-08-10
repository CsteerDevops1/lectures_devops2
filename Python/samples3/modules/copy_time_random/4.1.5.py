#!/usr/bin/env python3
"""
Псевдослучайные числа
"""
import random

random.random()        # Random float x, 0.0 <= x < 1.0
random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0

random.randint(1, 10)  # Integer from 1 to 10, endpoints included

random.randrange(0, 101, 2)  # Even integer from 0 to 100

random.choice("abcdefghij")  # Choose a random element

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print(items)

random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
