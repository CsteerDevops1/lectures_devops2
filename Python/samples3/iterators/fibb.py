#!/usr/bin/env python3


from collections.abc import Iterable

class Fibonacci(Iterable):
  def __init__(self):
    self.a, self.b = 0, 1
    self.total = 0
  def __iter__(self):
    return self
  def __next__(self):
    self.a, self.b = self.b, self.a + self.b
    self.total += self.a
    return self.a
  def running_sum(self):
    return self.total

fib = Fibonacci()
print(fib.running_sum())

for _, i in zip(range(10), fib):
  print(i, end=" ")

print(fib.running_sum())
print(next(fib))
print(fib.running_sum())
