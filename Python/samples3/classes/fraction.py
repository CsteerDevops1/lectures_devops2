#!/usr/bin/env python3

class Fr():
    @staticmethod
    def gcd(a, b):
        return a if b == 0 else Fr.gcd(b, a % b)

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError

        self.num = int(numerator / Fr.gcd(numerator, denominator))
        self.den = int(denominator / Fr.gcd(numerator, denominator))

    def __str__(self):
        return "0" if self.num == 0 else f"{self.num}/{self.den}"

    __repr__ = __str__

    def __add__(self, that):
        return Fr(self.num * that.den + that.num * self.den, self.den * that.den)

    def __sub__(self, that):
        return self + (-that)

    def __neg__(self):
        return Fr(-self.num, self.den)


if __name__ == "__main__":
    f = Fr(1, 2)
    e = Fr(1, 3)
    x = f - e
    print(f, e, x)
