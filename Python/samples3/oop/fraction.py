
#n/m
#n N
#m Z

class fr():
    def gcd(a,b): return a if b == 0 else gcd(b,a%b)
    def __init__(self, numerator, denominator):
        if denominator == 0: raise ZeroDivisionError
        self.num = int(numerator/gcd(numerator,denominator))
        self.den = int(denominator/gcd(numerator,denominator))
    def __str__(self):
        return '0' if self.num == 0 else f'{self.num}/{self.den}'
    __repr__ = __str__
    def __add__(self,that):
        return fr( self.num*that.den + that.num*self.den , self.den * that.den )
    def __sub__(self,that):
        return self + (-that)
    def __neg__(self):
        return fr(-self.num, self.den)



f = fr(1, 2)
e = fr(1, 3)

x = f - e



