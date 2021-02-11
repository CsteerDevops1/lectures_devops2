#!/usr/bin/env python3


def get_primes():
  "Simple lazy Sieve of Eratosthenes"
  candidate = 2
  found = []
  while True:
    if all(candidate % prime != 0 for prime in found):
      yield candidate
      found.append(candidate)
    candidate += 1

primes = get_primes()

next(primes), next(primes), next(primes)

for _, prime in zip(range(10), primes):
  print(prime, end=" ")

print()

from collections.abc import Sequence

class ExpandingSequence(Sequence):
  def __init__(self, it):
    self.it = it
    self._cache = []
  def __getitem__(self, index):
    while len(self._cache) <= index:
      self._cache.append(next(self.it))
    return self._cache[index]
  def __len__(self):
    return len(self._cache)

primes = ExpandingSequence(get_primes())

for _, p in zip(range(10), primes):
  print(p, end=" ")

print(primes[10])
print(primes[5])
print(len(primes))
print(primes[100])
print(len(primes))
