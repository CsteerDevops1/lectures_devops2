#!/usr/bin/env python3
""" This is not fraction2 module """

class Rational():
#  def gcd(a,b):
#    return a if b == 0 else gcd(b,a%b)
  def __init__(self,num,den):
    if den == 0:
      raise ZeroDivisionError
    self.num = num #int(num/gcd(num,den))
    self.den = den #int(den/gcd(num,den))
  def __str__(self):
    return f"R:{self.num}/{self.den}"
  def __repr__(self):
    return f"R:{self.num}/{self.den}"
  def __add__(self,other):
    """ this is add overloading """
    return Rational(self.num*other.den+self.den*other.num,self.den*other.den)
  def __sub__(self,other):
    return Rational(self.num*other.den-self.den*other.num,self.den*other.den)
  def __mul__(self,other):
    return Rational(self.num*other.num,self.den*other.den)
  def __truediv__(self,other):
    return Rational(self.num*other.den,self.den*other.num)
  def __neg__(self):
    return Rational(-self.num,self.den)
  def __len__(self):
    return len(str(self.num))+len(str(self.den))+1
  def __hidden(self):
    print("hidden method")

if __name__=="__main__":
  r1 = Rational(1,4)
  r2 = Rational(1,5)
  assert r1+r2 == Rational(9,20)
  print(r1+r2)
