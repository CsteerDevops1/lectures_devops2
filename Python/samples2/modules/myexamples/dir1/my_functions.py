def fib(n):
  #print(f'let us calculate fib for {n}')
  if n == 0 or n == 1 : return n
  return fib(n-2) + fib(n-1)

