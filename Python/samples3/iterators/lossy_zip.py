#!/usr/bin/python3

numbers = list(range(7))
print(numbers)
first_three, remaining = numbers[:3], numbers[3:]
print(first_three, remaining)
numbers_iter = iter(numbers)
print(list(zip(numbers_iter, first_three)))
# so far so good, let's zip the remaining
print(list(zip(numbers_iter, remaining)))
